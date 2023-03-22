# claimtcg
Code repository for trading card platform

## Image Recognition Pipeline
Use API Gateway to accept REST API requests for the data, and establish a WebSocket connection on the client side to return the image recognition query results. This approach can be used for any scenario where long-running queries are needed to provide responses to users.
  
![alt text](https://github.com/mcgigglepop/claimtcg/blob/main/images/image-recognition-pipeline.png?raw=true)
  
1. The Client generates an imageID UUID and uplaods the image to s3
2. The client sends a REST request to API Gateway with image UUID. This invokes a Lambda function that starts the Step Functions state machine execution. The function then returns the execution ID to the client.
3. Using the data returned by the REST request, the client connects to the WebSocket API and sends the Step Functions execution ID to the WebSocket connection.
4. The WebSocket triggers a Lambda function which creates a record in Dynamo DB. The record is a key-value mapping of Execution ARN – ConnectionId.
5. After RunImageRecognition is successful, Lambda will query DynamoDB to retrieve the ConnectionId associated with the current Execution.
6. Using the client-associated API Gateway WebSocket ConnectionId, Lambda updates the connected client over the WebSocket API that their long-running job is complete. It uses the REST API call post_to_connection.
7. The client receives the Image recognition data over their WebSocket connection using the IssueCallback Lambda function through the callback URL from the API Gateway WebSocket API.

## Appendix
### Local Build
python -m venv menv  
menv/scripts/activate  
$env:FLASK_APP = "app.py"  
$env:FLASK_DEBUG = 1 / 0  
pip install -r requirements.txt  
flask run  
  
### Build the docker Image  
docker build --tag REPOSITORY_NAME:tag .  
Run a container and publish over port 5000  
docker run REPOSITORY_NAME  
docker run --publish 5000:5000 523534f1  
Access the url to test locally in the browser  
Access cli docker exec -it keen_wilbur /bin/sh 
  
### Building the Database
flask db init  
flask db migrate -m "init"  
flask db upgrade  