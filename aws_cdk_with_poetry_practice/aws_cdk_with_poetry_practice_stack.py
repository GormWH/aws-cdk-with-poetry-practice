from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda,
)
from constructs import Construct

class AwsCdkWithPoetryPracticeStack(Stack):

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
