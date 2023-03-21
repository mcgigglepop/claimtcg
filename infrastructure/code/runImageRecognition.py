import json
import boto3
import os, time, datetime, sys
from urllib.parse import urlparse
import traceback


def lambda_handler(event, context):
    print(event)
    athena_client = boto3.client('athena', region_name=os.environ['region_name'])
    #discover if table exists, if not then create 
    athena_database = os.environ['athena_database']
    table_exists = tableExistsCheck(athena_database, os.environ['athena_table'],athena_client)
    if table_exists == 0:
        table_exists = createTable(os.environ['create_tweets_table'], athena_client, athena_database, os.environ['athena_table'])
        if table_exists == 0:
            event['s3_output_URL'] = "Athena table wasn't created"
            event['s3_bucket'] = "Athena table wasn't created"
            event['s3_key'] = "Athena table wasn't created"
            return 0
    
    # run query
    athena_result = run_query(event, athena_client)
    return event

def tableExistsCheck(athena_database, table, athena_client):
    print("Checking if DB: "+ athena_database + "." + table + " exists")
    query = "DESCRIBE "+athena_database+"."+table
    response = ''
    try:
        response = athena_client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={
                'Database': athena_database
            },
            ResultConfiguration={
                'OutputLocation': os.environ['s3_output_location']
            }
        )
        # wait for query to finish.
        queryrunning = 0
        while queryrunning == 0:
            # time.sleep(2)
            status = athena_client.get_query_execution(QueryExecutionId=response['QueryExecutionId'])
            results_file = status["QueryExecution"]["ResultConfiguration"]["OutputLocation"]
            if status["QueryExecution"]["Status"]["State"] != "RUNNING":
                queryrunning = 1
    except Exception as e:
        print("Exception: Database or Table not found " + athena_database + "." + table)
        print(e)
        print(traceback.format_exc()) 
        return 0
    return 1
    
def createTable(createTable, athena_client, athena_database, table):
    query = createTable
    print(query)
    response = ''
    try:
        response = athena_client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={
                'Database': athena_database
            },
            ResultConfiguration={
                'OutputLocation': os.environ['s3_output_location']
            }
        )
        print("Create table response: " + str(response))
        # wait for query to finish.
        queryrunning = 0
        while queryrunning == 0:
            time.sleep(2)
            status = athena_client.get_query_execution(QueryExecutionId=response['QueryExecutionId'])
            print(status)
            results_file = status["QueryExecution"]["ResultConfiguration"]["OutputLocation"]
            print(status["QueryExecution"]["Status"]["State"])
            if status["QueryExecution"]["Status"]["State"] != "RUNNING":
                queryrunning = 1
    except Exception as e:
        print("Exception: Database or Table could not be created " + athena_database + "." + table)
        print(e)
        print(traceback.format_exc()) 
        return 0
    return 1



def run_query(event, athena_client):
    athena_query = os.environ['athena_query']+"'"+event['Country']+"'"
    print("Athena Query: " + athena_query)
    athena_result = run_athena_query(athena_query, os.environ['athena_database'],
                                     os.environ['s3_output_location'], event, athena_client)
    return athena_result

# Runs athena query, open results file at specific s3 location and returns result
def run_athena_query(query, database, s3_output_location, event, athena_client):
    sf_client = boto3.client('stepfunctions')
    s3_client = boto3.client('s3', region_name=os.environ['region_name'])
    queryrunning = 0
    # Kickoff the Athena query
    response = athena_client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': database
        },
        ResultConfiguration={
            'OutputLocation': s3_output_location
        }
    )

    # Log the query execution id
    print('Execution ID: ' + response['QueryExecutionId'])

    # wait for query to finish.
    while queryrunning == 0:
        status = athena_client.get_query_execution(QueryExecutionId=response['QueryExecutionId'])
        results_file = status["QueryExecution"]["ResultConfiguration"]["OutputLocation"]
        if status["QueryExecution"]["Status"]["State"] != "RUNNING":
            queryrunning = 1

    # parse the s3 URL and find the bucket name and key name
    s3url = urlparse(results_file)
    s3_bucket = s3url.netloc
    s3_key = s3url.path
    
    event['s3_output_URL'] = "s3://"+s3_bucket+s3_key
    event['s3_bucket'] = s3_bucket
    event['s3_key'] = s3_key[1:]
    
    return event
