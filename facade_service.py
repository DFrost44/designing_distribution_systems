from flask import Flask, request, jsonify 
import hazelcast
import requests
import random
import uuid

import my_utils

app = Flask(__name__)

# msg_services = [
#     'http://localhost:9063/message',
#     'http://localhost:9064/message',
# ]

# log_services = [
#     'http://localhost:11003/log',
#     'http://localhost:11004/log',
#     'http://localhost:11005/log',
# ]



hz_addr = list(my_utils.get_key( f'hazelcast/address{p}') for p in range(3,6))
print(hz_addr)
clnt = hazelcast.HazelcastClient( cluster_members=hz_addr)

mq_name = my_utils.get_key('mq/name')
msgs = clnt.get_queue(mq_name).blocking()


@app.post("/")
def facade_post():
    msg = request.form['msg']
    msg_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, msg) 

    log_service_url = my_utils.random_choose_service('logging_service') + 'log'

    r = requests.post( log_service_url, data={ 'uuid':msg_uuid, 'msg':msg })
    msgs.offer( msg)
    return str( r.status_code ) + '\n'
 
@app.get('/')
def facade_get():
    log_service_url = my_utils.random_choose_service('logging_service') + 'log'
    msg_service_url = my_utils.random_choose_service('messages_service') + 'message'

    r1 = requests.get( log_service_url)
    r2 = requests.get( msg_service_url)
    return r1.text + ' : ' + r2.text


my_utils.register_service("facade_service", 9150, ['facade'])


