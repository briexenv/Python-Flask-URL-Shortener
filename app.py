#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, session
import json, string, random, validators
app = Flask(__name__)
configs = json.load(open('config.json', 'r'))
for key, value in configs.items():
  exec(key + '=value')

app.secret_key = secret_key

@app.route('/')
@app.route('/index')
def index():
  template = render_template('index.html')
  session.pop('url', None)
  session.pop('result', None)
  session.pop('status', None)
  return template


@app.route('/short', methods=['POST'])
def short_url():
  route, url = route_generator(), request.form['url']
  entry = {f'{route}':f'{url}'}
  if not validators.url(url):
    set_sessions("Error", "Invalid URL", "Please enter a valid url (ex: https://google.com)")
  else:
    with open(database, 'r+') as f:
      data = json.load(f)
      data.update(entry)
      f.seek(0)
      json.dump(data, f, indent = 4)
      set_sessions("Success", url, base_url + '/' + route)
  return redirect('/')
    
def route_generator(length = str_length, chars = string.ascii_uppercase + string.ascii_lowercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(length))

def set_sessions(status, url, result):
  session['status'] = status
  session['url'] = url
  session['result'] = result


@app.route('/<target>')
def goto(target):
  with open(database, 'r') as f:
    data = f.read()
    try:
      target = json.loads(data)[target]
      return redirect(target)
    except:
      return render_template('404.html')


if __name__ == '__main__':
  app.run(debug = True)