import boto3

#### creating a bucket named 'mybucket0231' ####

s3 = boto3.resource('s3')
bucket_name = 'mybucket0231'
bucket_result = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={ 'LocationConstraint': 'us-west-2'})

#### Uploading an image to the bucket 'mybucket0231' ####

with open('/home/cole/Downloads/test_image.jpg','rb') as fh:
    s3.Bucket(bucket_name).put_object(Key='test_image.jpg', Body=fh)
