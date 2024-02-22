#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from markupsafe import escape
import json


app = Flask(__name__)

status = None


### HTTP routes ----------------------------------------------------------------

@app.route('/')
def index():
    with open('status.txt', 'r') as f:
        for line in f:
            pass
        try:
            status_str = line
        except:
            status_str = ''
    status = json.loads(status_str)
    return render_template('index.html', status=status)

@app.route('/status')
def get_status():
    with open('status.txt', 'r') as f:
        for line in f:
            pass
        try:
            status_str = line
        except:
            status_str = ''
    return f"<p>{escape(status)}</p>"

@app.post('/status')
def post_status():
    global status
    status_str = request.form['data']
    status = json.loads(status_str)
    print(status)
    with open('status.txt', 'a') as f:
        f.write(str(status_str) + '\n')
    return "posted"


#if __name__ == '__main__':
#    if app.env == 'development':
#        socketio.run(app, host='0.0.0.0', port=80)
#    else:
#        socketio.run(app, port=5000)
