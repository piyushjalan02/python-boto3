# To create a new key pair and get PEM file.
# Make sure that aws credentials are set in ~/.aws/credentials and region is defined in ~/.aws/config

import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
	keypair = ec2.create_key_pair(KeyName='demo123')
        print(keypair['KeyMaterial'])
except ClientError as e:
        print(e)
