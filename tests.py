# import unittest
from flask.ext.testing import TestCase
from flask import Flask
import unittest
from requests import get
from models import Character, Person, Comic_Series, Power, Team, Publisher
from server import app, db
from requests import get

class FlaskModelTests(TestCase):

    def create_app(self):
    	app = Flask(__name__)
    	app.config['SQLALCHEMY_DATABASE_URI'] =  get('http://api.postgression.com').text
    	return app

    def setUp(self):
        db.drop_all()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_blank_character_creation(self):

	    character = Character(
	        id='1'
    	)
	    db.session.add(character)
	    db.session.commit()
	    c = Character.query.filter_by(id='1').first()
	    assert c.id == 1
	    assert c.name == None
	    assert c.gender == None
	    assert c.alias == None
	    assert c.description == None
	    assert c.origin == None

    def test_character_creation_1(self):

	    character = Character(
	        id='1',
	        name='Superman',
	        gender='Male',
	        alias='Clark Kent',
	        description='The invinsible Superman',
	        origin='Kryptonians',
    	)
	    db.session.add(character)
	    db.session.commit()
	    c = Character.query.filter_by(id='1').first()
	    assert c.id == 1
	    assert c.name == 'Superman'
	    assert c.gender == 'Male'
	    assert c.alias == 'Clark Kent'
	    assert c.description == 'The invinsible Superman'
	    assert c.origin == 'Kryptonians'
    def test_character_creation_2(self):

	    character = Character(
	        id='1004',
	        name='Batman',
	        gender='Male',
	        alias='Bruce Wayne',
	        description='Dark Knight',
	        origin='Human',
    	)
	    db.session.add(character)
	    db.session.commit()
	    c = Character.query.filter_by(id='1004').first()
	    assert c.id == 1004
	    assert c.name == 'Batman'
	    assert c.gender == 'Male'
	    assert c.alias == 'Bruce Wayne'
	    assert c.description == 'Dark Knight'
	    assert c.origin == 'Human'

    def test_blank_person_creation(self):

	    person = Person(
	        id='20'
		)
	    db.session.add(person)
	    db.session.commit()
	    c = Person.query.filter_by(id='20').first()
	    assert c.id == 20
	    assert c.name == None
	    assert c.country == None
	    assert c.job_title == None
	    assert c.website == None
	    assert c.gender == None

    def test_person_creation_1(self):

	    person = Person(
	        id='2000',
	        name='Bromethius',
	        country='Brossia',
	        job_title='Brah',
	        website='www.brodown.com',
	        gender='Bro'
		)
	    db.session.add(person)
	    db.session.commit()
	    c = Person.query.filter_by(id='2000').first()
	    assert c.id == 2000
	    assert c.name == 'Bromethius'
	    assert c.country == 'Brossia'
	    assert c.job_title == 'Brah'
	    assert c.website == 'www.brodown.com'
	    assert c.gender == 'Bro'
    
    def test_person_creation_2(self):

	    person = Person(
	        id='2001',
	        name='Zlatan',
	        country='Zlatan',
	        job_title='Footballer',
	        website='www.zlatan.com',
	        gender='God'
		)
	    db.session.add(person)
	    db.session.commit()
	    c = Person.query.filter_by(id='2001').first()
	    assert c.id == 2001
	    assert c.name == 'Zlatan'
	    assert c.country == 'Zlatan'
	    assert c.job_title == 'Footballer'
	    assert c.website == 'www.zlatan.com'
	    assert c.gender == 'God'

    def test_blank_comic_series(self):

	    comic = Comic_Series(
	        id='5',
		)
	    db.session.add(comic)
	    db.session.commit()
	    c = Comic_Series.query.filter_by(id='5').first()
	    assert c.id == 5
	    assert c.title == None
	    assert c.image == None
	    assert c.publisher_id == None

    def test_comic_series_creation_1(self):

	    comic = Comic_Series(
	        id='5',
	        title='Dark Knight',
	        image='pic',
		)
	    db.session.add(comic)
	    db.session.commit()
	    c = Comic_Series.query.filter_by(id='5').first()
	    assert c.id == 5
	    assert c.title == 'Dark Knight'
	    assert c.image == 'pic'

    def test_comic_series_creation_2(self):

	    comic = Comic_Series(
	        id='500',
	        title='Tower of God',
	        image='pic',
		)
	    db.session.add(comic)
	    db.session.commit()
	    c = Comic_Series.query.filter_by(id='500').first()
	    assert c.id == 500
	    assert c.title == 'Tower of God'
	    assert c.image == 'pic'

    def test_blank_publisher(self):

	    publisher = Publisher(
	        id='9',
		)
	    db.session.add(publisher)
	    db.session.commit()
	    c = Publisher.query.filter_by(id='9').first()
	    assert c.id == 9
	    assert c.name == None

    def test_publisher_creation_1(self):

	    publisher = Publisher(
	        id='90',
	        name='DC Comics'
		)
	    db.session.add(publisher)
	    db.session.commit()
	    c = Publisher.query.filter_by(id='90').first()
	    assert c.id == 90
	    assert c.name == 'DC Comics'

    def test_publisher_creation_2(self):

	    publisher = Publisher(
	        id='900',
	        name='Marvel'
		)
	    db.session.add(publisher)
	    db.session.commit()
	    c = Publisher.query.filter_by(id='900').first()
	    assert c.id == 900
	    assert c.name == 'Marvel'

    def test_blank_power(self):

	    power = Power(
	        id='14',
		)
	    db.session.add(power)
	    db.session.commit()
	    c = Power.query.filter_by(id='14').first()
	    assert c.id == 14
	    assert c.name == None

    def test_power_creation_1(self):

	    power = Power(
	        id='140',
	        name='Super Strength'
		)
	    db.session.add(power)
	    db.session.commit()
	    c = Power.query.filter_by(id='140').first()
	    assert c.id == 140
	    assert c.name == 'Super Strength'

    def test_power_creation_2(self):

	    power = Power(
	        id='1400',
	        name='Minute Man'
		)
	    db.session.add(power)
	    db.session.commit()
	    c = Power.query.filter_by(id='1400').first()
	    assert c.id == 1400
	    assert c.name == 'Minute Man'

    def test_blank_team(self):

	    team = Team(
	        id='38',
		)
	    db.session.add(team)
	    db.session.commit()
	    c = Team.query.filter_by(id='38').first()
	    assert c.id == 38
	    assert c.name == None

    def test_team_creation_1(self):

	    team = Team(
	        id='1409',
	        name='Justice League'
		)
	    db.session.add(team)
	    db.session.commit()
	    c = Team.query.filter_by(id='1409').first()
	    assert c.id == 1409
	    assert c.name == 'Justice League'

    def test_team_creation_2(self):

	    team = Team(
	        id='169',
	        name='Avengers'
		)
	    db.session.add(team)
	    db.session.commit()
	    c = Team.query.filter_by(id='169').first()
	    assert c.id == 169
	    assert c.name == 'Avengers'

if __name__ == '__main__':
    unittest.main()