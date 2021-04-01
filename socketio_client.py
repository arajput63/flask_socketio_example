import socketio
import datetime

server_address = "192.168.0.10"
server_port = 5000

sio = socketio.Client()

@sio.event
def connect():
    print("[ INFO ] Successfully connected to the server.")

@sio.event
def connect_error():
    print("[ INFO ] Failed to connect to the server.")

@sio.event
def disconnect():
    print("[ INFO ] Disconnected from the server.")


print('[ INFO ] Connecting to server http://{}:{}...'.format(
    server_address, server_port))

sio.connect(
    'http://{}:{}'.format(server_address, server_port),
    transports=['websocket'],
    namespaces=['/client']
)

