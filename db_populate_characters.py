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
    parsed = response.json()['results']

    character = models.Character(
        id=parsed['id'],
        name=parsed['name'],
        alias=parsed['aliases'],
        image=parsed['image']['medium_url'],
        description=parsed['deck'],
        gender=parsed['gender'],
        origin=parsed['origin']
    )
    db.session.add(character)
    db.session.commit()

