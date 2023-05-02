from flask import Flask, request, jsonify 
import requests
import random
import uuid


app = Flask(__name__)


# http://localhost:9150/        - facade 

# http://localhost:11003/log    - log1
# http://localhost:11004/log    - log2
# http://localhost:11005/log    - log3

# http://localhost:9152/mes     - message
log_services = [
    'http://localhost:11003/log',
    'http://localhost:11004/log',
    'http://localhost:11005/log',
]
def random_choose_log_service():
    return random.choice(log_services)

@app.post("/")
def facade_post():
    msg = request.form['msg']
    msg_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, msg) 

    log_service_url = random_choose_log_service()
    r = requests.post( log_service_url, data={ 'uuid':msg_uuid, 'msg':msg })
    
    return str( r.status_code ) + '\n'
 
@app.get('/')
def facade_get():
    log_service_url = random_choose_log_service()
    r1 = requests.get( log_service_url)
    r2 = requests.get('http://localhost:9152/message')
    return r1.text + ' : ' + r2.text

