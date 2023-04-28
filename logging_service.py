from flask import Flask, request, jsonify 

app = Flask(__name__)

msg_all = {}


@app.post("/log")
def put_to_database():
    msg_uuid = request.form['uuid']
    msg = request.form['msg']

    print(msg_uuid, '\t', msg)
    
    msg_all[msg_uuid] = msg
    
    return "Ok"

@app.get('/log')
def get_from_db():
    return ', '.join(msg_all.values())
