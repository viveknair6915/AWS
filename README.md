# AWS Lambda Functions

This repository contains AWS Lambda functions for common tasks, including adding two numbers and uploading files to an S3 bucket.

## Functions

### 1. Add Two Numbers Lambda
A Lambda function that accepts two numbers and returns their sum.

- **File**: `add_numbers_lambda.py`
- **Handler**: `add_numbers_lambda.lambda_handler`

### 2. Upload to S3 Lambda
A Lambda function that stores a document or PDF file in an S3 bucket.

- **File**: `upload_to_s3_lambda.py`
- **Handler**: `upload_to_s3_lambda.lambda_handler`

## Files

- `add_numbers_lambda.py`: Function to add two numbers.
- `upload_to_s3_lambda.py`: Function to upload a file to S3.
- `payload.json`: Example input data for testing.

## Setup

1. Clone this repository.
2. Configure AWS Lambda with the provided Python files.
3. Set up AWS IAM roles and permissions for S3 access.
4. Use `payload.json` for testing the functions locally
