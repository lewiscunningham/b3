import aws_cdk as core
import aws_cdk.assertions as assertions

from b3.b3_stack import B3Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in b3/b3_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = B3Stack(app, "b3")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
