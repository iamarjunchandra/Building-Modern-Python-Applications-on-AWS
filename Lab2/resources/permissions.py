import boto3
import json

S3API = boto3.client("s3", region_name="us-west-2") 
bucket_name = "c11284a122552l730173t1w440822749602-s3bucket-1v6wjklgyoqr7"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("DONE")