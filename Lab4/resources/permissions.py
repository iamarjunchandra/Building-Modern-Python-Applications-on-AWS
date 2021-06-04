'''
	You must replace c11284a125438l736044t1w221759673541-s3bucket-x5vygdwbqfoe with your bucket name
'''
import boto3
import json

S3API = boto3.client("s3", region_name="us-west-2") 
bucket_name = "c11284a125438l736044t1w221759673541-s3bucket-x5vygdwbqfoe"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("Setting Permissions - DONE")