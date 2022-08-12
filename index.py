import json
import boto3

s3_client = boto3.client("s3")
S3_BUCKET_NAME = 'smart-devl-sfbu-us-east-1'
#data to be written in this file
file_name = 'obj_file.txt'

def smart-devl3-servicing-python-lambda(event, context):
    # to read and list all objects
response = s3_client.list_objects_v2(
        Bucket=smart-devl-sfbu-us-east-1)
    s3_files = response["Contents"]
    for s3_file in s3_files:
        file_content = json.loads(s3_client.get_object(
            Bucket=smart-devl-sfbu-us-east-1, Key=s3_file["Key"])["Body"].read())
        print(file_content)
    # to write objects
client = boto3.client('s3')
s3_client.put_object(Body=file_name, Bucket='smart-devl-sfbu-us-east-1', Key=s3_file["Key"])
    # put data to db
    client_postgres = boto3.resource('rds-data')
    rResponse = client_postgres.put_item(
        TableName = 'bch_In', 'srvg_rcon',
        Item = file_name
    )
