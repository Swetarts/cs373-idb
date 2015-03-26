import unittest
from models import Character
from server import db

class BuildDestroyTables(unittest.TestCase):

    def setUp(self):
        db.drop_all()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_setup(self):

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

if __name__ == '__main__':
    unittest.main()