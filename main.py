from application import create_app
from flask_socketio import SocketIO
from flask import render_template


app = create_app()
socketio = SocketIO(app)

@app.route('/', methods = ['GET','POST'])
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_event(json, methods = ['GET','POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)



if __name__ == "__main__":
    socketio.run(app, debug = True)
