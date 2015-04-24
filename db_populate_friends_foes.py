# ---------------------------
# cs373-idb/db_populate_friends_foes.py
# Copyright (C) 2015
# Swetarts
# ---------------------------

from server import db
import models
import requests
import json

character_id_list = ['1807', '1440', '1696', '1486', '2349', '1698', '2048', '2267', '1443', '1699','1441','1442','1444','1445','1446','1449','1451','1453','1455','1456','1457','1459','1460','1461','1462','1464','1466','1467','1468','1469','1470','1475','1476','1477','1479','1480','1483','1485','1486','1487','1488','1489','1490','1499','1504','1505','1525','1573','1686','1691','1696','1697','1702','1780','1926','2111','2112','2113','2114','2120','2122','2126','2149','2151','2156','2157','2158','2175','2190','2242','2250','2268','2349','2351','2357','2635','3174','3176','3179','3182','3200','3202','3223','3228','3239','3336','3337','3338','3390','3423','3530','3544','3546','3548','3552','3554','3587','3588','3617','3715','3718','3725','3726','3727','3738','1253','4324','4333','4459','4562','4563','4917','5466','5547','5652','5936','6803','6805','6806','6807','7570','7606','7607','7608','7612']

request_url = 'http://www.comicvine.com/api/character/4005-'
payload = {'api_key':'83ff911e240812bc29cf73246626fe319a6a4b71', 'format':'json', 'field_list':'id,name,aliases,description,image,creators,gender,origin,powers,teams,character_friends,character_enemies', 'offset':'0'}
for char_id in list(character_id_list):
    print('#', end=' ')
    api_request = request_url + char_id + '/'
    response = requests.get(api_request, params=payload)
    num_results = response.json()['number_of_total_results']

    parsed = response.json()['results']
    
    id = parsed['id']
    # print(id)

    #Get character object from db
    character = db.session.query(models.Character).filter_by(id=int(id)).first()

    #Add allies
    allies = parsed['character_friends']
    for ally in list(allies):
        friend = db.session.query(models.Character).filter_by(id=int(ally['id'])).first()
        if friend:       
            character.allies.append(friend)
            # print(ally['id'], ally['name'])

    #Add enemies
    enemies = parsed['character_enemies']
    for enemy in list(enemies):
        nemesis = db.session.query(models.Character).filter_by(id=int(enemy['id'])).first()
        if nemesis:
            character.enemies.append(nemesis)
            # print(enemy['id'], enemy['name'])

    db.session.add(character)
    db.session.commit()
    # print('****************************************************************************************************')
