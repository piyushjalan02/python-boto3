#To create a new s3 bucket.
#Make sure that aws credentials are set in ~/.aws/credentials and region is defined in ~/.aws/config

import boto3

s3 = boto3.client("s3")
response = s3.create_bucket(Bucket="my-bucket-name", CreateBucketConfiguration={'LocationConstraint': 'ap-southeast-1'})
print ("Bucket created successfully!! %s" % response)
