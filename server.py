import requests
import json
from flask import *
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
app.debug = True
cors = CORS(app)


@app.route('/<filename>')
def files(filename):
  return send_from_directory('www', filename)

@app.route('/characters')
@cross_origin()
def get_characters():
  response = requests.get('http://www.comicvine.com/api/characters/?api_key=2a196eae09708f335bc341657e97155564ab9514&limit=10&format=json')
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)

@app.route('/characters/<id>')
@cross_origin()
def get_character_detail(id):
  request_url = 'http://www.comicvine.com/api/character/4005-{}?api_key=2a196eae09708f335bc341657e97155564ab9514&format=json'.format(id)
  response = requests.get(request_url)
  parsed = json.loads(response.content.decode())
  results = parsed['results']
  return json.dumps(results)


@app.route('/<any(controllers, templates, filters, services, bower_components):folder>/<path:filename>')
def toplevel_static(folder, filename):
  filename = safe_join(folder, filename)
  cache_timeout = app.get_send_file_max_age(filename)
  return send_from_directory('www', filename, cache_timeout=cache_timeout)

if __name__ == '__main__':
  app.run()
