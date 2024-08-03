# Data Pipeline with Reddit, Airflow, Celery, Postgres, S3, AWS Glue, Athena, and Redshift

### This project provides a comprehensive data pipeline solution to extract, transform, and load (ETL) Reddit data into a Redshift data warehouse. The pipeline leverages a combination of tools and services including Apache Airflow, Celery, PostgreSQL, Amazon S3, AWS Glue, Amazon Athena, and Amazon Redshift.

## Table of Contents

* Overview
* Architecture
* Prerequisites

# Overview

### The pipeline is designed to:

1. Extract data from Reddit using its API.
2. Store the raw data in an S3 bucket from Airflow.
3. Transform the data using AWS Glue and Amazon Athena.
4. Load the transformed data into Amazon Redshift for analytics and querying.

# Architecture

![Reddit_dataengineering](https://github.com/user-attachments/assets/03943ec4-8ccc-4dee-a85d-e3d4fbe67bf2)

1. Reddit API: Source of the data.
2. Apache Airflow & Celery: Orchestrates the ETL process and manages task distribution.
3. PostgreSQL: Temporary storage and metadata management.
4. Amazon S3: Raw data storage.
5. AWS Glue: Data cataloging and ETL jobs.
6. Amazon Athena: SQL-based data transformation.
7. Amazon Redshift: Data warehousing and analytics.

# Prerequisites
1. AWS Account with appropriate permissions for S3, Glue, Athena, and Redshift.
2. Reddit API credentials.
3. Docker Installation
4. Python 3.9 or higher


