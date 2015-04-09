# import unittest
from flask.ext.testing import TestCase
from flask import Flask
import unittest
from requests import get
from models import Character, Person, Comic_Volume, Power, Team, Publisher, Comic_Issue
from server import app, db
from requests import get

# ---------------
# FlaskModelTests
# ---------------

class FlaskModelTests(TestCase):

    def create_app(self):
        app = Flask(__name__)
        return app

    @classmethod
    def setUpClass(models):
        app.config['SQLALCHEMY_DATABASE_URI'] =  get('http://api.postgression.com').text.replace('postgres', 'postgresql') 
        # models.set_verbose(True)    
        db.drop_all()
        db.create_all()

    def tearDown(self):
        #remove ALL the models
        db.session.query(Character).delete()
        db.session.query(Person).delete()
        db.session.query(Comic_Volume).delete()
        db.session.query(Power).delete()
        db.session.query(Team).delete()
        db.session.query(Publisher).delete()
        db.session.query(Comic_Issue).delete()
        db.session.commit()


    # def setUp(self):
    #     app.config['SQLALCHEMY_DATABASE_URI'] =  get('http://api.postgression.com').text.replace('postgres', 'postgresql') 
    #     models.set_verbose(True)    
    #     db.drop_all()
    #     db.create_all()

    @classmethod
    def tearDownClass(models):
        db.session.remove()
        db.drop_all()

    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()

    # ---------------
    # Character Tests
    # ---------------

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
            id='1',
            name='Batman',
            gender='Male',
            alias='Bruce Wayne',
            description='Dark Knight',
            origin='Human',
      )
        db.session.add(character)
        db.session.commit()
        c = Character.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == 'Batman'
        assert c.gender == 'Male'
        assert c.alias == 'Bruce Wayne'
        assert c.description == 'Dark Knight'
        assert c.origin == 'Human'

    # ---------------
    # Person Tests
    #---------------

    def test_blank_person_creation(self):

        person = Person(
            id='1'
      )
        db.session.add(person)
        db.session.commit()
        c = Person.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == None
        assert c.country == None
        assert c.website == None
        assert c.gender == None

    def test_person_creation_1(self):

        person = Person(
            id='1',
            name='Bromethius',
            country='Brossia',
            website='www.brodown.com',
            gender='Bro'
      )
        db.session.add(person)
        db.session.commit()
        c = Person.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == 'Bromethius'
        assert c.country == 'Brossia'
        assert c.website == 'www.brodown.com'
        assert c.gender == 'Bro'
    
    def test_person_creation_2(self):

        person = Person(
            id='1',
            name='Zlatan',
            country='Zlatan',
            website='www.zlatan.com',
            gender='God'
      )
        db.session.add(person)
        db.session.commit()
        c = Person.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == 'Zlatan'
        assert c.country == 'Zlatan'
        assert c.website == 'www.zlatan.com'
        assert c.gender == 'God'

    # ------------------
    # Comic Issue Tests
    # ------------------

    def test_blank_comic_issue(self):

        comic = Comic_Issue(
            id='1',
      )
        db.session.add(comic)
        db.session.commit()
        c = Comic_Issue.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.title == None
        assert c.image == None

    def test_comic_issue_creation_1(self):

        comic = Comic_Issue(
            id='1',
            title='Dark Knight',
            image='pic',
      )
        db.session.add(comic)
        db.session.commit()
        c = Comic_Issue.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.title == 'Dark Knight'
        assert c.image == 'pic'

    def test_comic_issue_creation_2(self):

        comic = Comic_Issue(
            id='1',
            title='Tower of God',
            image='pic',
      )
        db.session.add(comic)
        db.session.commit()
        c = Comic_Issue.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.title == 'Tower of God'
        assert c.image == 'pic'

    # ---------------
    # Publisher Tests
    # ---------------

    def test_blank_publisher(self):

        publisher = Publisher(
            id='1',
      )
        db.session.add(publisher)
        db.session.commit()
        c = Publisher.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == None

    def test_publisher_creation_1(self):

        publisher = Publisher(
            id='1',
            name='DC Comics'
      )
        db.session.add(publisher)
        db.session.commit()
        c = Publisher.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == 'DC Comics'

    def test_publisher_creation_2(self):

        publisher = Publisher(
            id='1',
            name='Marvel'
      )
        db.session.add(publisher)
        db.session.commit()
        c = Publisher.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == 'Marvel'

    # ---------------
    # Power Tests
    # ---------------

    def test_blank_power(self):

        power = Power(
            id='1',
      )
        db.session.add(power)
        db.session.commit()
        c = Power.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == None

    def test_power_creation_1(self):

        power = Power(
            id='1',
            name='Super Strength'
      )
        db.session.add(power)
        db.session.commit()
        c = Power.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == 'Super Strength'

    def test_power_creation_2(self):

        power = Power(
            id='1',
            name='Minute Man'
      )
        db.session.add(power)
        db.session.commit()
        c = Power.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == 'Minute Man'

    # ----------
    # Team Tests
    # ----------

    def test_blank_team(self):

        team = Team(
            id='1',
      )
        db.session.add(team)
        db.session.commit()
        c = Team.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == None

    def test_team_creation_1(self):

        team = Team(
            id='1',
            name='Justice League'
      )
        db.session.add(team)
        db.session.commit()
        c = Team.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == 'Justice League'

    def test_team_creation_2(self):

        team = Team(
            id='1',
            name='Avengers'
      )
        db.session.add(team)
        db.session.commit()
        c = Team.query.filter_by(id='1').first()
        assert c.id == 1
        assert c.name == 'Avengers'

if __name__ == '__main__':
    unittest.main()