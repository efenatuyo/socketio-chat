from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('message')
def message(data):
    emit('message', data, broadcast=True)
    

socketio.run(app)