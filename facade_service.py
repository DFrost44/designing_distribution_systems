from flask import Flask, request, jsonify 
import hazelcast
import requests
import random
import uuid


app = Flask(__name__)


# http://localhost:9150/        - facade 

# http://localhost:11003/log    - log1
# http://localhost:11004/log    - log2
# http://localhost:11005/log    - log3

# http://localhost:9163/mes     - msg1
# http://localhost:9164/mes     - msg2

msg_services = [
    'http://localhost:9063/message',
    'http://localhost:9064/message',
]

log_services = [
    'http://localhost:11003/log',
    'http://localhost:11004/log',
    'http://localhost:11005/log',
]

clnt = hazelcast.HazelcastClient( cluster_members=["172.17.0.3:5701","172.17.0.4:5701","172.17.0.5:5701"])
msgs = clnt.get_queue('MQ').blocking()

def random_choose_service(services_list):
    return random.choice(services_list)

@app.post("/")
def facade_post():
    msg = request.form['msg']
    msg_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, msg) 

    log_service_url = random_choose_service(log_services)
    r = requests.post( log_service_url, data={ 'uuid':msg_uuid, 'msg':msg })
    msgs.offer( msg)
    return str( r.status_code ) + '\n'
 
@app.get('/')
def facade_get():
    log_service_url = random_choose_service(log_services)
    msg_service_url = random_choose_service(msg_services)
    r1 = requests.get( log_service_url)
    r2 = requests.get( msg_service_url)
    return r1.text + ' : ' + r2.text

