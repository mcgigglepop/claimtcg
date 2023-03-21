import sys, os, base64, datetime, hashlib, hmac,json
import boto3
from botocore.client import Config
ddbClient = boto3.client('dynamodb')


api_endpoint_url = os.environ['callbackURL']
splitUrl = api_endpoint_url.split(".")
api_region = splitUrl[2]
apiManagement = boto3.client('apigatewaymanagementapi', region_name=api_region,
                      endpoint_url=api_endpoint_url)
class DynamoRecordDoesNotExist(Exception):
        pass
def lambda_handler(event, context):
    print(vars(context))
    print("Input from invoke: " + str(event))

    s3_URL = event['myPayload']['s3_output_URL']
    s3_bucket = event['myPayload']['s3_bucket']
    s3_key = event['myPayload']['s3_key']

    currentExecutionArn = event['myArn']
    ddbGet = ddbClient.get_item(TableName='PollToPush-ExecutionMapper', Key={'ExecutionArn':{'S': currentExecutionArn}})
    if 'Item' in ddbGet:
        clientForCurrentExecution = ddbGet['Item']['WsClientId']['S']
        url = generate_presigned_s3(s3_bucket, s3_key, 900, clientForCurrentExecution)

        print(clientForCurrentExecution + " --> " + currentExecutionArn)

        response = apiManagement.post_to_connection(
                Data=url,
                ConnectionId=str(clientForCurrentExecution)
            )
        return event
    else:
        raise DynamoRecordDoesNotExist("Cannot find DynamoDB record which maps the current ExecutionArn to a connected WebSocket Client.")


# Generate Pre-signed URL 15 minute expiration
def generate_presigned_s3(bucket, key, expiration, connectionID):
    params = {
        'Bucket': bucket,
        'Key': key
    }
    s3 = boto3.client('s3', api_region, config=Config(s3={'addressing_style': 'path'}))
    url = s3.generate_presigned_url('get_object', Params=params, ExpiresIn=expiration)
    print("s3 pre-signed URL: " + url)
    return url
