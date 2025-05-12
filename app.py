#!/usr/bin/env python3

import os

import aws_cdk as cdk

#from integreat_analytics.integreat_analytics_stack import InteGreatAnalyticsStack


app = cdk.App()
InteGreatAnalyticsStack(app, "InteGreatAnalyticsStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()

"""
app.py

Main CDK entrypoint for deploying Integreat's analytics infrastructure.

Instructions for developers:
- Add or remove tenants in the TENANTS dictionary as needed.
  • Each tenant must specify their S3 bucket name and the path to their Python handler.
- Each tenant will be deployed with:
  • A Python Lambda function for exporting analytics to their S3 bucket
- All tenant Lambdas will be scheduled by a single EventBridge rule that triggers daily at 12MN (GMT+8).
- Integreat’s own Lambda (in scripts/integreat) runs the centralized DW ETL and uploads CSVs to each tenant bucket.
- No secrets manager is used; configuration is passed via CDK context or environment variables.
- S3 permissions must be managed in the separate Node.js infrastructure stack.
"""