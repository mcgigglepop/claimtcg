import json
import boto3
import os, time, datetime, sys
from urllib.parse import urlparse
import traceback


def lambda_handler(event, context):
    bucket = os.environ['BUCKET']
    key = event['Key']
    
    client=boto3.client('rekognition')
    detect_text = client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':key}})
    moderation_labels = client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':key}})

    event['detect_text'] = detect_text
    event['moderation_labels'] = moderation_labels

    return event