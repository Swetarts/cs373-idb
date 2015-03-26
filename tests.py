import unittest
from models import Character
from server import db

class FlaskModelTests(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()