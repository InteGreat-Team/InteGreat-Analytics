import aws_cdk as core
import aws_cdk.assertions as assertions

from inte_great_analytics.inte_great_analytics_stack import InteGreatAnalyticsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in inte_great_analytics/inte_great_analytics_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = InteGreatAnalyticsStack(app, "inte-great-analytics")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
