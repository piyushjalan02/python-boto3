import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('rsys-sonarqube')
total_size=0
for obj in bucket.objects.all():
    total_size += obj.size

total_size = total_size/1024/1024/1024
print "Total Bucket %s size is %d GB" % (bucket.name, total_size)
