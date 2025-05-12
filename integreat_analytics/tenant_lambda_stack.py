"""
tenant_lambda_stack.py

This CDK stack provisions a Python-based AWS Lambda function for a specific tenant
(e.g., Campus, Pillars, Teleo), using their corresponding handler script.

Responsibilities:
- Defines a PythonFunction Lambda with its code under scripts/<tenant>/handler.py
- Configures the Lambda with:
    • 2048 MB of memory (2GB)
    • 15-minute timeout (maximum allowed for AWS Lambda)
    • This also scales the vCPU to approximately 1 vCPU for the duration
- Passes environment/context variables to the Lambda for runtime config

Each tenant gets its own Lambda to run analytics exports independently.
This keeps data pipelines isolated and allows for custom logic per tenant.

Note:
- AWS Lambda does not automatically scale CPU or RAM per invocation
- CPU is scaled proportionally to memory (2GB ≈ 1 vCPU)
- To improve performance, memory must be manually increased
- S3 access is assumed to be provisioned and granted in a separate stack
"""
