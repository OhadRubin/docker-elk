#app.py
from flask import Flask, request, abort
from logging.handlers import SocketHandler


class FlaskTCPLogstashHandler(SocketHandler, object):
    def __init__(self, host, port=50000):
        super(FlaskTCPLogstashHandler, self).__init__(host, port)
    def makePickle(self, record):
        
        return record + b'\n'
app = Flask(__name__)

handler = FlaskTCPLogstashHandler("logstash", 50000)
@app.route('/log', methods=['POST'])
def log():
    username = request.headers.get('Username')
    password = request.headers.get('Password')
    if username == 'your_username' and password == 'your_password':
        handler.emit(request.data)
        return 'OK', 200
    else:
        abort(401)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5557)