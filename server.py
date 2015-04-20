import requests
import json
from flask import *
from flask.ext.cors import CORS, cross_origin
from flask.ext.sqlalchemy import SQLAlchemy
from flask.json import jsonify
import config
import subprocess
from sqlalchemy.exc import *

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
@app.route('/<any(assets, templates,  bower_components, dist):folder>/<path:filename>')
def toplevel_static(folder, filename):
  filename = safe_join(folder, filename)
  cache_timeout = app.get_send_file_max_age(filename)
  return send_from_directory('www', filename)

# defines the behavior of a HTTP get characters request
@app.route('/api/characters')
@cross_origin()
def get_characters():
  try:
    results = json.dumps([i.serialize_clipped for i in db.session.query(models.Character).all()])
  except Exception as e:
    print("GAGGOT" + str(e))
    request_url = 'http://www.comicvine.com/api/characters/?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'
    response = requests.get(request_url)
    parsed = json.loads(response.content.decode())
    p = parsed['results']
    results = json.dumps(p)

  return results

# defines the behavior of a HTTP get a single characters request
@app.route('/api/characters/<id>')
@cross_origin()
def get_character_detail(id):
  try:
    result = json.dumps(db.session.query(models.Character).filter_by(id=id).first().serialize)
  except Exception as e:
    print("GAGGOT" + str(e))
    request_url = 'http://www.comicvine.com/api/character/4005-{}?api_key=2a196eae09708f335bc341657e97155564ab9514&format=json'.format(id)
    print(request_url)
    response = requests.get(request_url)
    parsed = json.loads(response.content.decode())
    p = parsed['results']
    result = json.dumps(p)

  return result

# defines the behavior of a HTTP get request for people
@app.route('/api/people/')
@cross_origin()
def get_people():
  try:
    results = json.dumps([i.serialize_clipped for i in db.session.query(models.Person).all()])
  except Exception:
    request_url = 'http://www.comicvine.com/api/people?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=5&format=json'
    response = requests.get(request_url)
    parsed = json.loads(response.content.decode())
    p = parsed['results']
    results = json.dumps(p)

  return results

# defines the behavior of a HTTP get request for a single person
@app.route('/api/people/<id>')
@cross_origin()
def get_person(id):
  try:
    result = json.dumps(models.Person.query.filter_by(id=id).first().serialize)
  except Exception:
    request_url = 'http://www.comicvine.com/api/person/4040-{}?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'.format(id)
    response = requests.get(request_url)
    parsed = json.loads(response.content.decode())
    p = parsed['results']
    result = json.dumps(p)

  return result

# defines the behavior of a HTTP get request for all issues
@app.route('/api/issues/')
@cross_origin()
def get_issues():
  try:
    results = json.dumps([i.serialize_clipped for i in db.session.query(models.Comic_Issue).all()])
  except NotImplementedError:
    request_url = 'http://www.comicvine.com/api/issues?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'
    response = requests.get(request_url)
    parsed = json.loads(response.content.decode())
    p = parsed['results']
    results = json.dumps(p)

  return results

#  defines the behavior of a HTTP get request for a single issue
@app.route('/api/issues/<id>')
@cross_origin()
def get_issue_detail(id):
  try:
    raise NotImplementedError
  except NotImplementedError:
    request_url = 'http://www.comicvine.com/api/issue/4000-{}?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json'.format(id)
    response = requests.get(request_url)
    parsed = json.loads(response.content.decode())
    p = parsed['results']
    results = json.dumps(p)

  return results

@app.route('/api/tests')
def run_tests():
  print("Running tests")
  script = subprocess.Popen("python tests.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  try:
    outs, errs = script.communicate()
  except:
    script.kill()
  print(outs.decode())
  errs = errs.decode()
  return json.dumps({"results": errs})

@app.route('/api/search')
def search():
  query = models.Character.query.search('Batman')
  print(query.all())
  print(type(query))
  return json.dumps({"results": "hi"})


if __name__ == '__main__':
  app.run(host='0.0.0.0')
