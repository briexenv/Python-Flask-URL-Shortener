#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/short', methods=['POST'])
def short_url():
  route, url = request.form['key'], request.form['url']
  entry = {f'{route}':f'{url}'}
  with open('static/urls.json', 'r+') as f:
    data = json.load(f)
    data.update(entry)
    f.seek(0)
    json.dump(data, f)
    return '{"status":"OK"}'

@app.route('/<target>')
def goto(target):
  with open('static/urls.json', 'r') as f:
    data = f.read()
  target = json.loads(data)[target]
  return redirect(target)

if __name__ == '__main__':
  app.run(debug = True)