#To upload a file on S3 bucket.
#Make sure that aws credentials are set in ~/.aws/credentials and region is defined in ~/.aws/config

import boto3

s3=boto3.client('s3')

#Pass your bucket name and file name to upload on S3.
s3.put_object(Bucket='my-bucket-name', Key='my.txt')
