# ---------------------------
# cs373-idb/db_populate_characters.py
# Copyright (C) 2015
# Swetarts
# ---------------------------

from server import db
import models
import requests
import json

character_id_list = ['1807', '1440', '1696', '1486', '2349', '1698', '2048', '2267', '1443', '1699']

request_url = 'http://www.comicvine.com/api/character/4005-'
payload = {'api_key':'83ff911e240812bc29cf73246626fe319a6a4b71', 'format':'json', 'field_list':'id,name,aliases,description,image,creators,gender,origin,powers,teams,character_friends,character_enemies', 'offset':'0'}
for char_id in list(character_id_list):
    api_request = request_url + char_id + '/'
    response = requests.get(api_request, params=payload)
    num_results = response.json()['number_of_total_results']

    parsed = response.json()['results']
    
    id = parsed['id']
    # print(id)

    name = parsed['name']
    # print(name)

    #This is ugly but some alias lists are delimited by \r\n and some just \n
    alias = parsed['aliases'].split('\n')[0].split('\r')[0]
    # print(alias)

    images = parsed['image']['thumb_url']
    # print(images)

    description = parsed['description']
    # print(description)

    gender = 'male' if parsed['gender'] == 1 else 'female'
    # print(gender)

    origin = parsed['origin']['name']
    # print(origin)

    #Create a new character object
    character = models.Character(id=int(id), name=name, alias=alias, image=images, description=description, gender=gender, origin=origin)

    #Add power objects
    powers = parsed['powers']
    for power in list(powers):
        character.powers.append(db.session.query(models.Power).filter_by(id=int(power['id'])).first())
        # print(power['id'], power['name'])

    #Add team objects
    teams = parsed['teams']
    for team in list(teams):
        character.teams.append(db.session.query(models.Team).filter_by(id=int(team['id'])).first())
        # print(team['id'], team['name'])

    # #Add allies
    # allies = parsed['character_friends']
    # for ally in list(allies):
    #     friend = db.session.query(models.Character).filter_by(id=int(ally['id'])).first()
    #     if friend:       
    #         character.allies.append(friend)
    #         # print(ally['id'], ally['name'])

    # #Add enemies
    # enemies = parsed['character_enemies']
    # for enemy in list(enemies):
    #     nemesis = db.session.query(models.Character).filter_by(id=int(enemy['id'])).first()
    #     if nemesis:
    #         character.enemies.append(nemesis)
    #         # print(enemy['id'], enemy['name'])

    #Add creators
    creators = parsed['creators']
    for creator in list(creators):
        person = db.session.query(models.Person).filter_by(id=int(creator['id'])).first()
        if person:
            character.creators.append(person)
            # print(creator['id'], creator['name'])

    db.session.add(character)
    db.session.commit()
    # print('****************************************************************************************************')
