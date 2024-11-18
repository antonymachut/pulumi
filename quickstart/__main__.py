"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage
import os
import json

google_credentials = os.getenv("GOOGLE_CREDENTIALS")
if google_credentials:
    credentials = json.loads(google_credentials)
    # Configure les authentifications si nécessaire


# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('my-bucket', location="US")

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)
