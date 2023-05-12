from flask import Flask, request, jsonify 
import hazelcast
import sys

try:
    p = int(sys.argv[1])
except:
    p=3

app = Flask(__name__)

msg_all = {}
clnt = hazelcast.HazelcastClient( cluster_members=[f"172.17.0.{p}:5701",])
msgs = clnt.get_map('User_Messages').blocking()

@app.post("/log")
def put_to_database():
    msg_uuid = request.form['uuid']
    msg = request.form['msg']

    print(msg_uuid, '\t', msg)
    
    msgs.set(msg_uuid, msg)
    
    return "Ok"

@app.get('/log')
def get_from_db():
    return ', '.join(msgs.values())

 
if __name__ == '__main__':
    app.run(debug=True, port=( 11000 + int(sys.argv[1])))
