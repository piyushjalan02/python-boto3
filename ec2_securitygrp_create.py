import boto3
from botocore.exceptions import ClientError
ec2 = boto3.client('ec2')
try:
    response = ec2.describe_vpcs()
    vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
    print("VPC id : - {0}".format(vpc_id))
    security_group = ec2.create_security_group(
        Description='Your security grp',
        GroupName='Your_security',
        VpcId=vpc_id
    )    
    data = ec2.authorize_security_group_ingress(
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