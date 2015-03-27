# ---------------------------
# cs373-idb/db_populate_comics.py
# Copyright (C) 2015
# Swetarts
# ---------------------------

from server import db
import models
import requests
import json

comic_id_list = ['362496', '2267', '308947', '120834', '105483', '245832', '468444', '434071', '225808', '359962']

request_url = 'http://www.comicvine.com/api/issue/4000-'
payload = {'api_key':'83ff911e240812bc29cf73246626fe319a6a4b71', 'format':'json', 'field_list':'id,name,image,cover_date,person_credits,character_credits,volume', 'offset':'0'}
for comic_id in list(comic_id_list):
    api_request = request_url + comic_id + '/'
    response = requests.get(api_request, params=payload)
    num_results = response.json()['number_of_total_results']

    parsed = response.json()['results']
    
    id = parsed['id']
    # print(id)

    title = parsed['name']
    # print(name)

    image = parsed['image']['icon_url']
    # print(images)

    launch_date = parsed['cover_date'].split(' ')[0]
    # print(launch_date)

    volume_id = parsed['volume']['id']
    volume_request = 'http://www.comicvine.com/api/volume/4050-'
    vol_payload = {'api_key':'83ff911e240812bc29cf73246626fe319a6a4b71', 'format':'json', 'field_list':'id,publisher'}
    vol_request = volume_request + str(volume_id) + '/'
    vol_response = requests.get(vol_request, params=vol_payload)
    publisher_id = vol_response.json()['results']['publisher']['id']
    # print(publisher_id)

    comic = models.Comic_Series(id=int(id), title=title, image=image, launch_date=launch_date, publisher_id=publisher_id)

    #Add featured characters
    characters = parsed['character_credits']
    for character in list(characters):
        hero = db.session.query(models.Character).filter_by(id=int(character['id'])).first()
        if hero:
            comic.characters.append(hero)
        # print(ally['id'], ally['name'])

    #Add featured people
    creators = parsed['person_credits']
    for creator in list(creators):
        person = db.session.query(models.Person).filter_by(id=int(creator['id'])).first()
        if person:
            comic.people.append(person)

    db.session.add(comic)
    db.session.commit()
    # print('****************************************************************************************************')