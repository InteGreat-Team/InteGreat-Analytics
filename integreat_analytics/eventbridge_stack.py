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