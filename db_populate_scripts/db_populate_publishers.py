# ---------------------------
# cs373-idb/db_populate_publishers.py
# Copyright (C) 2015
# Swetarts
# ---------------------------

from server import db
import models
import requests
import json

request_url = 'http://www.comicvine.com/api/publishers/'
payload = {'api_key':'83ff911e240812bc29cf73246626fe319a6a4b71', 'format':'json', 'field_list':'name,id,image,location_address,location_city,location_state,deck', 'offset':'0'}
response = requests.get(request_url, params=payload)
num_results = response.json()['number_of_total_results']
while True:
    response = requests.get(request_url, params=payload)
    parsed = response.json()['results']

    for x in list(parsed):
        id = x['id']
        # print(id)

        name = x['name']
        # print(name)

        if(x['image'] == None):
            image = 'None'
        else:
            image = x['image']['thumb_url']
        # print(image)

        location_address = x['location_address']
        # print(location_address)

        location_city = x['location_city']
        # print(location_city)

        location_state = x['location_state']
        # print(location_state)
        
        description = x['deck']
        # print(description)

        publisher = models.Publisher(id=int(id), name=name, image=image, location_address=location_address, location_city=location_city, location_state=location_state, description=description)
        db.session.add(publisher)
        db.session.commit()

    payload['offset'] = str(int(payload['offset']) + 100) 
    if int(payload['offset']) > int(num_results):
    	break

