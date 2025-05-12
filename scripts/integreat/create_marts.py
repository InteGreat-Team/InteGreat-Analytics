"""
create_marts.py

Step 2 of the ETL pipeline.

This script generates or refreshes materialized views inside Integreat's
OLAP schema. These views serve as pre-filtered "data marts" for each tenant.

Each materialized view isolates data relevant to a specific tenant:
- All API calls made by that tenant
- All API calls made to that tenant by other applications

Unlike the OLAP fact and dimension tables (which are shared across tenants),
each materialized view contains only the subset of data needed by the target tenant.

Power BI cannot connect directly to NeonDB, so these views are exported to CSV
files (via a later step) and uploaded to S3 for tenant-specific dashboarding.

Tasks:
- Connect to Integreat's NeonDB instance
- For each tenant:
    - Create or replace a materialized view in Integreat's OLAP schema
    - Name the views consistently for later CSV export

Note:
- These views are never created in tenant databases
- Each view is owned and maintained by Integreat
"""