# To launch a new VPC in a specific region.
# Make sure that aws credentials are set in ~/.aws/credentials and region is defined in ~/.aws/config

import boto3
from botocore.exceptions import ClientError            
ec2=boto3.resource('ec2', region_name='us-west-1')
try:
	vpc = ec2.create_vpc(CidrBlock='192.168.0.0/16')
	vpc.create_tags(Tags=[{"Key": "Demo-VPC", "Value":""}])
	vpc.wait_until_available()
except ClientError as e:
	print(e)
print(vpc.id)
