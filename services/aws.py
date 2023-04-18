import boto3

dynamodb = boto3.resource('dynamodb')

s3 = boto3.client("s3")

ses = boto3.client("ses")
