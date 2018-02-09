# To launch a new instance in a region.
# Make sure that aws credentials are set in ~/.aws/credentials and region is defined in ~/.aws/config

import boto3

ec2 = boto3.resource('ec2', region_name='ap-southeast-1')
launch_instances = ec2.create_instances(
  MinCount=1, MaxCount=1, ImageId='ami-8765849',
  InstanceType='t2.nano', SubnetId='subnet-ah674j8d8') 
for instance in launch_instances:
  print("Waiting for the instance to be running state")
  instance.wait_until_running()
  instance.reload()
  print("Instance id = %s " % instance.id)
  print("Instance state = %s " % instance.state['Name'])
