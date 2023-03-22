# claimtcg
Code repository for trading card platform

## Local Build
python -m venv menv  
menv/scripts/activate  
$env:FLASK_APP = "app.py"  
$env:FLASK_DEBUG = 1 / 0  
pip install -r requirements.txt  
flask run  
  
# Build the docker Image  
docker build --tag REPOSITORY_NAME:tag .  
Run a container and publish over port 5000  
docker run REPOSITORY_NAME  
docker run --publish 5000:5000 523534f1  
Access the url to test locally in the browser  
Access cli docker exec -it keen_wilbur /bin/sh 
  
## Building the Database
flask db init  
flask db migrate -m "init"  
flask db upgrade  