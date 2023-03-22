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

    finalPayload = {}
    
    detectText = event['myPayload']['detect_text']
    moderationLabels = event['myPayload']['moderation_labels']

    finalPayload['detect_text'] = detectText
    finalPayload['moderation_labels'] = moderationLabels

    currentExecutionArn = event['myArn']
    
    ddbGet = ddbClient.get_item(TableName='ImageRecognition-ExecutionMapper', Key={'ExecutionArn':{'S': currentExecutionArn}})

    if 'Item' in ddbGet:
        clientForCurrentExecution = ddbGet['Item']['WsClientId']['S']

        print(clientForCurrentExecution + " --> " + currentExecutionArn)

        response = apiManagement.post_to_connection(
                Data=str(finalPayload),
                ConnectionId=str(clientForCurrentExecution)
            )
        return event
    else:
        raise DynamoRecordDoesNotExist("Cannot find DynamoDB record which maps the current ExecutionArn to a connected WebSocket Client.")
