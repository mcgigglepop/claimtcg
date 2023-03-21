import boto3

def lambda_handler(event, context):
    executionArn = event['queryStringParameters']['ExecutionArn']
    client = boto3.client('stepfunctions')
    describe_response = client.describe_execution(
        executionArn=executionArn
    )
    if describe_response == '':
        return {
          'statusCode': 502,
          'body': 'Invalid Execution ARN'
        }
    body = "{\"Status\" : \""+describe_response['status']+"\""
    if describe_response['status'] == 'RUNNING':
        body += ",\"Input\" : \""+describe_response['input']+"\" }"
    else:
        body += ",\"Output\" : \""+describe_response['output']+"\" }"
    print("describe response input ")
    print(describe_response)
    return {
        'statusCode': 200,
        'body': body
    }