from gevent.pywsgi import WSGIServer
from app import app
import argparse

parser = argparse.ArgumentParser(description='Run the server')
parser.add_argument('--port', type=int, default=8888, help='Port to run the server on')

server_port = parser.parse_args().port

http_server = WSGIServer(("0.0.0.0", server_port), app)
http_server.serve_forever()