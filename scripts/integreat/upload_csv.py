"""
upload_csv.py

Step 3 of the ETL pipeline.

This script extracts data from Integreat’s OLAP schema — including
fact tables, dimension tables, and materialized views per tenant —
converts the data to CSV format, and uploads the resulting files
to the appropriate S3 buckets for consumption by Power BI.

Since Power BI cannot directly query NeonDB, this export step is
critical for enabling tenant-level analytics in Power BI via CSVs.

Tasks:
- Connect to Integreat’s NeonDB instance
- For each tenant:
    - Query OLAP fact and dimension tables
    - Query the tenant's materialized view (data mart)
    - Convert each result to a CSV file (timestamped)
    - Upload each CSV to that tenant’s S3 bucket

CSV Naming Convention:
- sales-fact-YYYY-MM-DD.csv
- product-dim-YYYY-MM-DD.csv
- time-dim-YYYY-MM-DD.csv
- mart-<tenant>-YYYY-MM-DD.csv

Assumptions:
- Tenant bucket names are pre-configured
- Files are saved to /tmp before upload (Lambda-compatible)
"""
