"""
etl_to_olap.py

Step 1 of the ETL pipeline.

This script extracts raw API transaction data from Integreat's OLTP table
(`api_transaction`), performs transformation logic, and loads the results into
Integreat's centralized OLAP schema using a star schema design (facts and dimensions).

This OLAP schema acts as the single source of truth for analytics across all tenants.

Tasks:
- Connect to Integreat's NeonDB instance
- Read from the OLTP schema (`api_transaction`)
- Create or replace dimension tables
- Create or replace fact tables
- Insert transformed data into the centralized OLAP schema

Assumptions:
- Only Integreat can access the OLAP schema
- Timestamp-based filtering is used for incremental loads
- Materialized views will later be generated for each tenant based on this OLAP data
"""
