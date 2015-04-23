# ---------------------------
# cs373-idb/db_populate_people.py
# Copyright (C) 2015
# Swetarts
# ---------------------------

from server import db
import models
import requests
import json

people_id_list = ['40467', '5614', '43591', '19137', '40755', '3439', '7365', '3380', '41171', '4026','40467','5614','40382','40841','7082','40468','3380','41468','40724','40893','1251','1252','1270','1280','1293','1299','1302','1303','1325','1326','1349','1350','1351','1352','1361','1385','1429','1433','1435','1436','1437','1509','1513','1514','1515','1516','1524','1531','1533','1537','1539','1540','1541','1543','1547','1575','1598','1602','1610','1613','1635','1642','1645','1647','1656','1657','1658','1662','1663','1664','1669','1672','1673','1675','1676','1678','1679','1693','1700','1703','1704','1732','1733','1734','1751','1752','1760','1761','1764','1768','1769','1770','1772','1773','1774','1775','1785','1795','1796','1804','1805','1806','1811','1812','1816','1817','1824','1825','1827','1828','1839','1840','1841','1905','1906','1915','1916','1921','1922','1923']

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

    country = parsed['country']
    # print(country)

    description = parsed['deck']
    # print(description)

    website = parsed['website']
    # print(website)

    gender = 'male' if parsed['gender'] == 1 else 'female'
    # print(gender)

    #Create a new person object
    person = models.Person(id=int(id), name=name, image=image, birth_date=birth_date, country=country, description=description, gender=gender)

    db.session.add(person)
    db.session.commit()
    # print('****************************************************************************************************')
