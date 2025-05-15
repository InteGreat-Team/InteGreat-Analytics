"""
eventbridge_stack.py

This CDK stack creates an EventBridge rule (cron scheduler) that triggers
a target Lambda function at a defined interval (e.g., daily at 12 midnight).

Responsibilities:
- Defines a rule using EventBridge Schedule (cron)
- Binds the rule to the specified tenant Lambda

This scheduler is used to automate analytics extraction and upload for each tenant.
The trigger time is set to match the operational timezone (e.g., GMT+8 for 12MN).
"""

from aws_cdk import (
    Stack,
    aws_events as events,
    aws_events_targets as targets,
    aws_lambda as lambda_
)
from constructs import Construct

class EventBridgeStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define tenants
        tenants = ['campus', 'evntgarde', 'pillars', 'teleo']

        # Create EventBridge rule for each tenant
        for tenant in tenants:
            # Create rule that triggers daily at 12:00 AM GMT+8
            rule = events.Rule(
                self, f"{tenant.title()}AnalyticsRule",
                schedule=events.Schedule.cron(
                    minute='0',
                    hour='0',
                    day='*',
                    month='*',
                    year='*'
                ),
                description=f"Daily trigger for {tenant} analytics export"
            )

            # Get the Lambda function
            fn = lambda_.Function.from_function_name(
                self, f"{tenant.title()}AnalyticsLambda",
                function_name=f"{tenant}-analytics-handler"
            )

            # Add Lambda as target for the rule
            rule.add_target(targets.LambdaFunction(fn))