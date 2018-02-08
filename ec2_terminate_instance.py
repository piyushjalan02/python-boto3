# To terminate an EC2 instance.
# Make sure that aws credentials are set in ~/.aws/credentials and region is defined in ~/.aws/config

import boto3

ec2=boto3.client('ec2')
ec2.terminate_instances(InstanceIds=['i-0f1975840385793'])
print "Instance terminated successfully !!!"

