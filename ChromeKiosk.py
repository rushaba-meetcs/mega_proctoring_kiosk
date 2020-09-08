from flask import Flask
from flask import request
import sys
from flask import render_template
import os
import keyboard
from flaskwebgui import FlaskUI
import socket
import os, sys
import threading
from multiprocessing import Process


base_dir = '.'
if hasattr(sys, '_MEIPASS'):
    base_dir = os.path.join(sys._MEIPASS)

app = Flask(__name__,
        static_folder=os.path.join(base_dir, 'static'),
        template_folder=os.path.join(base_dir, 'templates'))
#ui = FlaskUI(app,fullscreen=True)





class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
     while True:
        keyboard.add_hotkey("win", lambda: None, suppress =True)
        keyboard.add_hotkey("f1", lambda: None, suppress =True)
        keyboard.add_hotkey("alt+f4", lambda: None, suppress =True)
        keyboard.add_hotkey("alt+esc", lambda: None, suppress =True)
        keyboard.add_hotkey("alt+tab", lambda: None, suppress =True)
        keyboard.add_hotkey("alt", lambda: None, suppress =True)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    

@app.route('/is_connected', methods=['GET'])
def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return "True"
    except OSError:
        pass
    return "False"


@app.route('/1')
def keydisable():
    keyboard.add_hotkey("alt + f4", lambda: None, suppress =True)
    keyboard.add_hotkey("win", suppress =True)
    return 'disable'
@app.route('/exit')
def exit_app():
    shutdown_server()
    
    return 'Server shutting down...'

@app.route('/no_internet')
def no_internet():
    return render_template('internet_error.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/')
def init_page():
   
    return render_template('init_page.html')

        

@app.route('/data',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("main.html",result = result)
   

if __name__ == '__main__':
    global thread1
    thread1 = myThread(1, "Thread-1", 1)
    thread1.start()
    #os.system('taskkill /im chrome.exe')
    os.system('start chrome "http://127.0.0.1:5000/" --kiosk')
    #os.system('start chrome "http://127.0.0.1:5000/"')
    
    # keyboard.add_hotkey("f1", lambda: None, suppress =True)
    # keyboard.add_hotkey("alt+f4", lambda: None, suppress =True)
    # keyboard.add_hotkey("alt+esc", lambda: None, suppress =True)
    # keyboard.add_hotkey("alt", lambda: None, suppress =True)
    #ui.run()
    import logging
    logging.basicConfig(filename='error.log',level=logging.DEBUG)
    app.run()
   
    
    
