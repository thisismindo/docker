# Overview
Flask application using python and docker

# Requirements
- docker >= 23.0.x
- python >= 3.10.x
    - gunicorn >= 20.1.x
    - flask >= 2.2.x
    - flask-httpauth >= 4.7.x
    - flask-restful >= 0.3.x

# Setup
- setup api service
```sh
make up
```
- test rest api endpoint
```sh
curl http://localhost:4040/api/v1/user/1

expected response:
{"status": true, "body": {"user": {"id": "1"}}}
```

# Tear down
- clean this project locally
```sh
make down || make reset
```
