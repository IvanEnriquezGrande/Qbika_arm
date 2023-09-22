from flask import Flask, render_template, Response, request
from flask_socketio import SocketIO
import base64


def create_app():
    app = Flask(__name__)

    socketio = SocketIO(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @socketio.on('connect')
    def handle_connect():
        print('WebSocket client connected')

    @socketio.on('disconnect')
    def handle_disconnect():
        print('WebSocket client disconnected')

    @socketio.on('image_data')
    def handle_image_data(image_data):
        try:
            img_bytes = base64.b64decode(image_data)

            socketio.emit('display_image', image_data, broadcast=True)
        except Exception as e:
            print(f"Error handling image data: {str(e)}")

    return app
