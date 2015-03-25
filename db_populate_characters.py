# ---------------------------
# cs373-idb/db_populate_characters.py
# Copyright (C) 2015
# Swetarts
# ---------------------------

from server import db
import models
import requests
import json

character_id_list = ['1807', '1440', '1696', '1486', '2349', '1698', '2048', '1469', '1443', '1699']

request_url = 'http://www.comicvine.com/api/character/4005-'
payload = {'api_key':'83ff911e240812bc29cf73246626fe319a6a4b71', 'format':'json', 'field_list':'id,name,aliases,deck,image,creators,gender,origin,powers,teams,character_friends,character_enemies', 'offset':'0'}
for char_id in list(character_id_list):
    api_request = request_url + char_id + '/'
    response = requests.get(api_request, params=payload)
    num_results = response.json()['number_of_total_results']
    response = requests.get(api_request, params=payload)
    print(response.json())
    # parsed = response.json()['results']
    # id = parsed['id']
    # teams = parsed['teams']
    print(id)
    print('****************************************************************************************************')
    # break
    # for x in list(parsed):
	   #  # print(x['id'], x['name'])
    #     team = models.Team(id=x['id'], name=x['name'])
    #     db.session.add(team)
    #     db.session.commit()

    # payload['offset'] = str(int(payload['offset']) + 100) 
    # if int(payload['offset']) > int(num_results):
    # 	break

