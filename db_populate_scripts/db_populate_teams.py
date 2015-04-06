# ---------------------------
# cs373-idb/db_populate_teams.py
# Copyright (C) 2015
# Swetarts
# ---------------------------

from server import db
import models
import requests
import json

request_url = 'http://www.comicvine.com/api/teams/'
payload = {'api_key':'83ff911e240812bc29cf73246626fe319a6a4b71', 'format':'json', 'field_list':'name,id,deck', 'offset':'0'}
response = requests.get(request_url, params=payload)
num_results = response.json()['number_of_total_results']
while True:
    response = requests.get(request_url, params=payload)
    parsed = response.json()['results']

    for x in list(parsed):
	    # print(x['id'], x['name'], x['deck'])
        team = models.Team(id=int(x['id']), name=x['name'], description=x['deck'])
        db.session.add(team)
        db.session.commit()

    payload['offset'] = str(int(payload['offset']) + 100) 
    if int(payload['offset']) > int(num_results):
    	break

