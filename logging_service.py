from flask import Flask, request, jsonify 
import hazelcast
import my_utils

import sys

try:
    p = int(sys.argv[1])
except:
    p=3

app = Flask(__name__)

msg_all = {}

hz_addr = my_utils.get_key( f'hazelcast/address{p}')
print(hz_addr)
clnt = hazelcast.HazelcastClient( cluster_members=[hz_addr])

map_name = my_utils.get_key( 'hazelcast/map_name')
msgs = clnt.get_map(map_name).blocking()


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
    port=( 11000 + int(sys.argv[1]))
    my_utils.register_service( f"logging_service_{p}", port, ['logging'])
    app.run(host="0.0.0.0", debug=True, port=port)
