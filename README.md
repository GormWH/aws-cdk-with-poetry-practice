# AWS CDK with Poetry practice

This is a practice project to use AWS CDK with Python and Poetry to manage dependencies.

In this project, I will change the default CDK project structure to use Poetry for dependency management.
And then I will create a simple Lambda function using CDK.

## How I created this project

### Prerequisites

- AWS CLI installed and configured ([Configuring settings for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html))
- AWS CDK installed ([Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
  - npm installed
- Poetry installed ([Poetry installation](https://python-poetry.org/docs/#installation))

### Steps

1. Create a new directory for the project and move to the directory.

    ```bash
    mkdir <project name>
    cd <project name>
    ```

2. Initialize a new CDK project.

    ```bash
    cdk init app --language python
    ```

    The command creates a new CDK project with the following structure:

    ```plaintext
    .
    ├── <project_name>/
    ├── tests/
    ├── README.md
    ├── app.py
    ├── cdk.json
    ├── requirements.txt
    ├── requirements-dev.txt
    └── .gitignore
    ```

3. Initialize a new Poetry project.

    ```bash
    poetry init -q
    ```

   Above command creates a pyproject.toml file in the project directory.

4. Add the following dependencies to the pyproject.toml file.

    ```toml
    [tool.poetry]
    ...

    [tool.poetry.dependencies]
    python = "^3.12"
    aws-cdk-lib = "==2.165.0"
    constructs = "10.*"

    [tool.poetry.group.dev.dependencies]
    pytest = "8.*"

    [build-system]
    ...
    ```

    Note that the `aws-cdk-lib` and `constructs` dependencies are from `requirements.txt` and `requirements-dev.txt` files which are created by the CDK.
    The version format of these dependencies are converted to the format that Poetry can understand.

    ```plaintext
    # requirements.txt
    aws-cdk-lib==2.165.0
    constructs>=10.0.0,<11.0.0
    
    # pyproject.toml
    aws-cdk-lib = "==2.165.0"
    constructs = "10.*"
    ```

5. Install the dependencies.

    ```bash
    poetry install
    ```

6. Test CDK deployment.

    ```bash
    poetry run cdk deploy
    ```

    If you get an error like `SSM parameter /cdk-bootstrap/xxxx not found`, you need to bootstrap the CDK environment and try again.

    ```bash
    poetry run cdk bootstrap
    poetry run cdk deploy
    ```

7. Remove unnecessary files.

    ```bash
    rm -rf .venv  # since we are using Poetry, we don't need the virtual environment created by CDK
    rm requirements.txt requirements-dev.txt source.bat  # dependencies are managed by Poetry not requirements.txt etc.
    ```

## Creating simple Lambda function

1. Create a python file for lambda handler.

    ```bash
    mkdir src
    mkdir src/handlers
    touch src/handlers/hello_world.py
    ```

    And the file content is:

    ```python
    # src/handlers/hello_world.py
    import json


    def handler(event: dict, context: dict):
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Hello, World!"
            })
        }

    ```

2. Create a Lambda function using CDK.

    In the `<project_name>/<project_name>_stack.py` file, add the following code:

    ```python
    from aws_cdk import (
        # Duration,
        Stack,
        aws_lambda,
    )
    from constructs import Construct

    class <project_name_in_pascal_case>Stack(Stack):

        def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
            super().__init__(scope, construct_id, **kwargs)

            # The code that defines your stack goes here

            hello_world_lambda_function = aws_lambda.Function(
                self,
                id='HelloWorldLambdaFunction',
                runtime=aws_lambda.Runtime.PYTHON_3_12,
                code=aws_lambda.Code.from_asset('src/handlers'),
                handler='hello_world.handler',
            )
    ```

3. Re-deploy the CDK stack.

    ```bash
    poetry run cdk deploy
    ```

    After the deployment, you can see the Lambda function in the AWS console.
