# ---------------------------
# cs373-idb/db_populate_people.py
# Copyright (C) 2015
# Swetarts
# ---------------------------

from server import db
import models
import requests
import json

people_id_list = ['40467', '5614', '43591', '19137', '40755', '3439', '7365', '3380', '41171', '4026']

request_url = 'http://www.comicvine.com/api/person/4040-'
payload = {'api_key':'83ff911e240812bc29cf73246626fe319a6a4b71', 'format':'json', 'field_list':'id,name,image,birth,country,deck,website,gender', 'offset':'0'}
for people_id in list(people_id_list):
    api_request = request_url + people_id + '/'
    response = requests.get(api_request, params=payload)
    num_results = response.json()['number_of_total_results']

    parsed = response.json()['results']
    
    id = parsed['id']
    # print(id)

    name = parsed['name']
    # print(name)

    image = parsed['image']['icon_url']
    # print(image)

    birth_date = parsed['birth'].split(' ')[0]
    # print(birth_date)

    #This is not an accurate lable, may need to change in future release
    job_title = parsed['deck']
    # print(job_title)

    website = parsed['website']
    # print(website)

    gender = 'male' if parsed['gender'] == 1 else 'female'
    # print(gender)

    #Create a new person object
    person = models.People(id=id, name=name, image=image, birth_date=birth_date, job_title=job_title, gender=gender)

    db.session.add(person)
    db.session.commit()
    # print('****************************************************************************************************')