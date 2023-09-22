from GUI.app import create_app
from flask_socketio import SocketIO, emit


app = create_app()
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, debug=True)
