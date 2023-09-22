import sys
import time
import cv2 as cv
import ecal.core.core as ecal_core
from ecal.core.publisher import ProtoPublisher
import Proto.mensaje_main_pb2 as mensaje_main_pb2
import base64
import numpy as np
import websocket


def close_ws_and_ecal(ws):
    # Close the WebSocket connection and finalize eCAL properly
    ws.close()
    ecal_core.finalize()
    cv.destroyAllWindows()


def on_error(ws, error):
    print(f"WebSocket Error: {error}")

def on_message(ws, message):
    # Define a callback function to handle received messages (image data)
    # In this example, we assume that the received message is a base64-encoded image
    img_bytes = base64.b64decode(message)

    # Process the received image data as needed
    # For example, display the image using OpenCV
    img = cv.imdecode(np.frombuffer(img_bytes, dtype=np.uint8), cv.IMREAD_COLOR)
    cv.imshow('Received Image', img)
    cv.waitKey(1)


try:
    ecal_core.initialize(sys.argv, "Python webcam Publisher")

    websocket_url = 'ws://127.0.0.1:5000'
    ws = websocket.WebSocketApp(websocket_url, on_message=on_message, on_error=on_error)

    pub = ProtoPublisher("webcam_data",
                         mensaje_main_pb2.webcam)
    protobuf_message = mensaje_main_pb2.webcam()
    cam = cv.VideoCapture(0)

    while ecal_core.ok():
        # OpenCV related
        ret_val, img = cam.read()

        if ret_val:
            # Encode the image as JPEG and convert it to a base64-encoded string
            _, img_encoded = cv.imencode('.jpg', img)
            img_base64 = base64.b64encode(img_encoded.tobytes()).decode('utf-8')
            if ws.sock:
                ws.send(img_base64)
            else:
                print("WebSocket connection is not open.")
            # Send the base64-encoded image data via WebSocket to the Flask app
            ws.send(img_base64)

            # eCAL-protobuf related
            protobuf_message.frame.height = img.shape[0]
            protobuf_message.frame.width = img.shape[1]
            protobuf_message.frame.name = "nombre-camara"
            protobuf_message.frame.data = img.data.tobytes()
            pub.send(protobuf_message)
        # pub.send(protobuf_message)
except KeyboardInterrupt:
    pass
finally:
    close_ws_and_ecal(ws)
