import requests
import json
from flask import *
from flask.ext.cors import CORS, cross_origin
from flask.ext.sqlalchemy import SQLAlchemy
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

# when you load up the index html page this cathces
# any asset, template, or bower component to properly send them
# to avoid a 404
@app.route('/<any(assets, templates,  bower_components):folder>/<path:filename>')
def toplevel_static(folder, filename):
  filename = safe_join(folder, filename)
  cache_timeout = app.get_send_file_max_age(filename)
  return send_from_directory('www', filename)

# defines the behavior of a HTTP get characters request
@app.route('/api/characters')
@cross_origin()
def get_characters():
  request_url = 'http://www.comicvine.com/api/characters/?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'
  response = requests.get(request_url)
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)

# defines the behavior of a HTTP get a single characters request
@app.route('/api/characters/<id>')
@cross_origin()
def get_character_detail(id):
  request_url = 'http://www.comicvine.com/api/character/4005-{}?api_key=2a196eae09708f335bc341657e97155564ab9514&format=json'.format(id)
  response = requests.get(request_url)
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)

# defines the behavior of a HTTP get request for people
@app.route('/api/people/')
@cross_origin()
def get_people():
  request_url = 'http://www.comicvine.com/api/people?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'
  response = requests.get(request_url)
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)

# defines the behavior of a HTTP get request for a single person
@app.route('/api/people/<id>')
@cross_origin()
def get_person(id):
  request_url = 'http://www.comicvine.com/api/person/4040-{}?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'.format(id)
  response = requests.get(request_url)
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)

# defines the behavior of a HTTP get request for all issues
@app.route('/api/issues/')
@cross_origin()
def get_issues():
  request_url = 'http://www.comicvine.com/api/issues?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'
  response = requests.get(request_url)
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)

#  defines the behavior of a HTTP get request for a single issue
@app.route('/api/issues/<id>')
@cross_origin()
def get_issue_detail(id):
  request_url = 'http://www.comicvine.com/api/issue/4000-{}?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'.format(id)
  response = requests.get(request_url)
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)

if __name__ == '__main__':
  app.run()
