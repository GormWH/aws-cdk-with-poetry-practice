import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_cdk_with_poetry_practice.aws_cdk_with_poetry_practice_stack import AwsCdkWithPoetryPracticeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_cdk_with_poetry_practice/aws_cdk_with_poetry_practice_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsCdkWithPoetryPracticeStack(app, "aws-cdk-with-poetry-practice")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
