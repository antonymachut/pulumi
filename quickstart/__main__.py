"""A Google Cloud Python Pulumi program"""

import pulumi
import pulumi_gcp as gcp
from pulumi_gcp import storage

gcp.config.credentials = pulumi.Config().require_secret("gcp:credentials")

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('my-bucket', location="US")

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)
