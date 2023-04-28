from flask import Flask

app = Flask(__name__)

@app.get("/message")
def message_get():
    return "This service hasn't been implemented yet"
