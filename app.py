from flask import Flask, render_template, url_for
from flask_socketio import SocketIO


print(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'ded!'
socketio = SocketIO(app)


@app.route('/')
def index():
	print(url_for('hello')) #to get url of specific route
	return render_template('index.html')


def messageReceived(method=['GET','POST']):
	print('Message Received!')


@socketio.on('my event')
def handle_my_custom_event(json, method=['GET','POST']):
	print(json)
	print('Received my event: ' + str(json))
	socketio.emit('My Response', json, callback=messageReceived())


#Tralling Slash Concept

'''
If tralling slash is present then /hi and /hi/ both will redirect to /hi/
Else if tralling slash is not available then /hi is valid endpoind, /hi/ will not founds
'''


@app.route('/hi')
def hello():
	return '<h1>Hello</h1>'


if __name__ == '__main__':
	print('True')
	socketio.run(app, debug=True)