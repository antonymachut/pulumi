"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage
import os
import base64
import json

encoded_credentials = os.getenv("GOOGLE_CREDENTIALS")
if encoded_credentials:
    decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
    credentials = json.loads(decoded_credentials)
    print("Service Account chargé avec succès !")
else:
    raise ValueError("La variable d'environnement GOOGLE_CREDENTIALS est introuvable.")




# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('my-bucket', location="US")

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)
