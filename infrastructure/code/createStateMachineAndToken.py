import boto3
import os 

def lambda_handler(event, context):
    print(event['queryStringParameters'])

    client = boto3.client('stepfunctions')

    imageKey = event['queryStringParameters']['Key']

    exec_response = client.start_execution(
        stateMachineArn=os.environ.get('stepfunctions_arn'),
        input="{\"Key\" : \""+imageKey+"\" }"
    )
    
    #capture executionArn
    executionArn = exec_response['executionArn']
    executionId = executionArn.split(':')[-1]

    task_token = 'x' 
    print(task_token)

    body = '{ "task_token" :"'+ task_token + '", "executionArn":"'+executionId+'"}'
    print(body)
    
    return {
        'statusCode': 200,
        'body': body, 
        'headers':{
            "Access-Control-Allow-Origin":"*"
        }
    }