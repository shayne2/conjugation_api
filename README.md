# conjugame_api
Sanic api used to get proper conjugation of verb given context

## Setup
$ python3.6 -m pip install -r requirements.txt


## Local Dev
$ python3.6 main.py


## Deployment
$ sudo docker build -t conjugame .

$ sudo docker run -d -p 8000:80 --name webserver conjugame

$ curl -d '{"context": ["Eu preciso","a mesa"], "verb": "pôr"}' 'http://<SERVER_OR_LOCALHOST>:8000/conjugate'
