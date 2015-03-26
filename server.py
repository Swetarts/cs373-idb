import requests
import json
from flask import *
from flask.ext.cors import CORS, cross_origin
from flask.ext.sqlalchemy import SQLAlchemy
from flask.json import jsonify
import config

app = Flask(__name__)
# Development settings 
app.config.from_object('config.DevelopmentConfig')
# Production settings
# app.config.from_object('config.ProductionConfig')
cors = CORS(app)
db = SQLAlchemy(app)

import models

# Catch all route to correctly handle manually
# entered URLs and send them to Angular
@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def index(**kwargs):
  return send_from_directory('www', 'index.html')

@app.route('/<any(assets, templates,  bower_components):folder>/<path:filename>')
def toplevel_static(folder, filename):
  filename = safe_join(folder, filename)
  cache_timeout = app.get_send_file_max_age(filename)
  return send_from_directory('www', filename)

@app.route('/api/characters')
@cross_origin()
def get_characters():
  # request_url = 'http://www.comicvine.com/api/characters/?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'
  # response = requests.get(request_url)
  # parsed = json.loads(response.content.decode())
  # results = parsed['results']
  # return json.dumps(results)
  return json.dumps([i.serialize for i in db.session.query(models.Character).all()])

@app.route('/api/characters/<id>')
@cross_origin()
def get_character_detail(id):
  request_url = 'http://www.comicvine.com/api/character/4005-{}?api_key=2a196eae09708f335bc341657e97155564ab9514&format=json'.format(id)
  response = requests.get(request_url)
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)

@app.route('/api/people/')
@cross_origin()
def get_people():
  request_url = 'http://www.comicvine.com/api/people?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'
  response = requests.get(request_url)
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)

@app.route('/api/people/<id>')
@cross_origin()
def get_person(id):
  request_url = 'http://www.comicvine.com/api/person/4040-{}?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'.format(id)
  response = requests.get(request_url)
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)

@app.route('/api/issues/')
@cross_origin()
def get_issues():
  request_url = 'http://www.comicvine.com/api/issues?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'
  response = requests.get(request_url)
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)

@app.route('/api/issues/<id>')
@cross_origin()
def get_issue_detail(id):
  request_url = 'http://www.comicvine.com/api/issue/4000-{}?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'.format(id)
  response = requests.get(request_url)
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)

@app.route('/api/test')
def get_test():
  return json.dumps([i.serialize for i in db.session.query(models.Character).all()])

if __name__ == '__main__':
  app.run()
