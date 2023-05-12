from flask import Flask
from flask_socketio import SocketIO
import hazelcast

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

clnt = hazelcast.HazelcastClient( cluster_members=[f"172.17.0.{p}:5701",])
msgs = clnt.get_queue('MQ').blocking()

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
    socketio.run(app, debug=True, port=( 9060 + int(sys.argv[1])),use_reloader=False)