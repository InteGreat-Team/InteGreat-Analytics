"""
__init__.py

Acts as the central coordinator for the Integreat analytics ETL process.

This file ties together the following steps:
1. Extract from OLTP.api_transaction table
2. Transform and load to tenant-specific OLAP schemas
3. Create or refresh materialized views per tenant (data marts)
4. Convert OLAP tables and views to CSV format
5. Upload all output to the appropriate S3 buckets

This module is executed by the Integreat Lambda function on a scheduled basis.
"""
from .etl_to_olap import run_etl
from .create_marts import create_materialized_views
from .upload_csv import upload_to_s3

def main():
    run_etl()
    create_materialized_views()
    upload_to_s3()