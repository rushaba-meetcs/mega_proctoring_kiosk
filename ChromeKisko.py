from flask import Flask
from flask import request
import sys
from flask import render_template
import os
import keyboard


app = Flask(__name__)
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
@app.route('/1')
def keydisable():
    keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
    keyboard.add_hotkey("win", suppress =True)
    return 'disable'
@app.route('/2')
def keyenable():
    shutdown_server()
    return 'Server shutting down...'
@app.route('/')
@app.route('/login')
def login():
    return render_template('home.html')


   

if __name__ == '__main__':
    keyboard.add_hotkey("win", lambda: None, suppress =True)
    os.system('taskkill /im chrome.exe')
    os.system('start chrome "http://127.0.0.1:5000/" --kiosk')
    keyboard.add_hotkey("f1", lambda: None, suppress =True)
    keyboard.add_hotkey("alt+f4", lambda: None, suppress =True)
    keyboard.add_hotkey("alt+esc", lambda: None, suppress =True)
    keyboard.add_hotkey("alt", lambda: None, suppress =True)
    app.run(debug=True)
    
