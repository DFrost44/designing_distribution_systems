from flask import Flask
from flask_socketio import SocketIO
import hazelcast
import my_utils

import random
import time
import sys


app = Flask(__name__)
socketio = SocketIO(app)

try:
    p = int(sys.argv[1])
except:
    p=3


local_db = []


@app.get("/message")
def message_get():
    global local_db
    print( f"local_db: {local_db}")
    localdb2 = local_db.copy()
    local_db = []
    return localdb2


mq_addr = my_utils.get_key('mq/address')
clnt = hazelcast.HazelcastClient( cluster_members=[mq_addr,])

mq_name = my_utils.get_key('mq/name')
msgs = clnt.get_queue(mq_name).blocking()

def run_localdb():
    global local_db

    while True:
        msg = msgs.poll()
        
        if msg:
            local_db.append(msg)
            print( f'MSG_{p} Appended {msg} into local db')

        time.sleep(2+random.random())


if __name__ == '__main__':
    socketio.start_background_task(run_localdb)
    
    port=( 9060 + int(sys.argv[1]))

    my_utils.register_service( "messages_service", port, [f'messages_{p}'])
    socketio.run(app, host="0.0.0.0", debug=True, port=port,use_reloader=False)
