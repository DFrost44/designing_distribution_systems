from flask import Flask, request, jsonify 
import requests
import uuid


app = Flask(__name__)


# http://localhost:9150/        - facade 
# http://localhost:9151/log     - log
# http://localhost:9152/mes     - message

@app.post("/")
def facade_post():
    msg = request.form['msg']
    msg_uuid = uuid.uuid3(uuid.NAMESPACE_DNS, msg) 
    r = requests.post('http://localhost:9151/log', data={ 'uuid':msg_uuid, 'msg':msg })
    return str( r.status_code ) + '\n'
 
@app.get('/')
def facade_get():
    r1 = requests.get('http://localhost:9151/log')
    r2 = requests.get('http://localhost:9152/message')
    return r1.text + ' : ' + r2.text

