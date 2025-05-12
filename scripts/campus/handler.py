"""
Campus Tribe – handler.py

This Lambda function connects to the Campus NeonDB instance,
queries the latest analytics data, exports it to CSV, and uploads
it to the Campus tribe’s dedicated S3 bucket for Power BI reporting.
"""