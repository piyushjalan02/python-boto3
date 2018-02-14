import boto3
from botocore.exceptions import ClientError
ec2=boto3.resource('ec2', region_name='us-east-1')
try:
	vpc = ec2.create_vpc(CidrBlock='192.168.0.0/16')
	vpc.create_tags(Tags=[{"Key": "Demo-VPC", "Value":""}])
	vpc.wait_until_available()
	ec2_client = boto3.client('ec2', region_name='us-east-1')
	security_group = ec2_client.create_security_group(Description='Boto3 security grp', GroupName='BOTO3_security', VpcId=vpc.id)
	print(security_group['GroupId'])
	data = ec2_client.authorize_security_group_ingress(
        GroupId=security_group['GroupId'],
	IpPermissions=[
	    {
	        'IpProtocol' : 'tcp',
	        'FromPort': 80,
	        'ToPort' : 80,
	        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
	    {
	        'IpProtocol': 'tcp',
	        'FromPort': 22,
	        'ToPort': 22,
	        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
	    }
	])
	print('Ingress Successfully Set %s' % data)
except ClientError as e:
	print(e)
