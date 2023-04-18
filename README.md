# Stori transactions - challenge

## Project summary

The project consist of two modules:

1. Web-API
2. Lambda Function

### WEB - API

This repo corresponds to the Lambda Function, which contain the handler for the trigger when a .csv file is uploaded to
an S3 Bucket, it will parse the file and insert the transactions to DynamoDB, then it will retrieve all the DynamoDB
data to compute the summary and send it via email using AWS SES.

Since this project implements the same functions for file parsing, DynamoDB inserts, DynamoDB reads, summary computing,
and email sending that are in the Web-API project but without an API, here isn't provided a Postman collection. This
project is deployed on AWS Lambda and is triggerd by the Web-API project. 