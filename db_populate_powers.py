# ---------------------------
# cs373-idb/db_populate_powers.py
# Copyright (C) 2015
# Swetarts
# ---------------------------

from server import db
import models
import requests
import json

request_url = 'http://www.comicvine.com/api/powers/'
payload = {'api_key':'83ff911e240812bc29cf73246626fe319a6a4b71', 'format':'json', 'field_list':'name,id'}
response = requests.get(request_url, params=payload)
parsed = response.json()['results']

for x in list(parsed):
	# print(x['id'], x['name'])
    power = models.Power(id=x['id'], name=x['name'])
    db.session.add(power)
    db.session.commit()

payload['offset'] = '100'    
response = requests.get(request_url, params=payload)
parsed = response.json()['results']

for x in list(parsed):
	# print(x['id'], x['name'])
    power = models.Power(id=x['id'], name=x['name'])
    db.session.add(power)
    db.session.commit()