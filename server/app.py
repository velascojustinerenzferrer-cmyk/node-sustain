import serial
import threading
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")


def serial_listener():

    try:
        ser = serial.Serial('COM3', 9600, timeout=1) 
        print("Successfully connected to the Bridge (Arduino).")
        
        while True:
            
            line = ser.readline().decode('utf-8').strip()
            
            if line:
                print(f"Hardware Trigger Detected: {line}")
                
                socketio.emit('update_ui', {
                    'uid': line,
                    'status': 'Verified'
                })
    except Exception as e:
        print(f"Bridge Error: {e}. Check your USB connection!")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    
    threading.Thread(target=serial_listener, daemon=True).start()
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
