import boto3
import os
import json
client = boto3.client('stepfunctions')
ddbClient = boto3.client('dynamodb')

def lambda_handler(event, context):
    print(event)
    messageBody = json.loads(event['body'])
    task_token = messageBody['task_token']
    executionArn = os.environ.get('stepfunctions_arn') + ":"+ str(messageBody['executionArn'])
    print("Execution ARN: " + executionArn)

    ddbClient.put_item(
    Item={
        'ExecutionArn': {
            'S': executionArn,
        },
        'WsClientId': {
            'S': event['requestContext']['connectionId'],
        },
    },
    TableName='PollToPush-ExecutionMapper',
)
                    
    return {
        'statusCode': 200,
        'body': event['requestContext']['connectionId']
    }