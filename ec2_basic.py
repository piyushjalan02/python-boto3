import boto3

ec2=boto3.resource('ec2')
for instance in ec2.instances.all():
     print("Public IP=%s" % instance.public_ip_address)
     print("Key pair=%s" % instance.key_name)
     print("Instance Type=%s" % instance.instance_type)
     print("Image ID=%s" % instance.image_id)
     print("VPC ID=%s" % instance.vpc_id)
     print("State= %s" % instance.state)
     print("\n")

