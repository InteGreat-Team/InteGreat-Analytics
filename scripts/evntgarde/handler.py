"""
EventGarde Tribe – handler.py

This Lambda queries EventGarde’s NeonDB for current analytics,
exports a flat snapshot to CSV, and uploads it to their S3 bucket
for consumption by Power BI dashboards.
"""