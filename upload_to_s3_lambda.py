import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Extract information from the event
        bucket_name = event['bucket_name']  # Name of the S3 bucket
        file_name = event['file_name']      # Desired file name (e.g., 'document.pdf')
        file_content_base64 = event['file_content']  # Base64 encoded content
        
        # Decode the base64 content
        file_content = base64.b64decode(file_content_base64)
        
        # Upload the file to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'File {file_name} successfully uploaded to {bucket_name}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
