import boto3
import json

S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "c183057a4714707l13714550t1w646510366650-s3bucket-2ketvqxzp8hs"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("Setting Permissions - DONE")