from server import db
import flask.ext.whooshalchemy

############
# M:N Tables
############
"""These are the many to many relationship tables that SQLAlchemy will
automatically reference. They just contain relationships to foreign keys
of connecting tables
"""

character_powers = db.Table('character_powers',
    db.Column('character_id', db.Integer, db.ForeignKey('character.id')),
    db.Column('power_id',     db.Integer,     db.ForeignKey('power.id'))
)

character_team = db.Table('character_team',
    db.Column('character_id', db.Integer, db.ForeignKey('character.id')),
    db.Column('team_id',      db.Integer, db.ForeignKey('team.id'))
)

character_ally = db.Table('character_ally',
    db.Column('character_id', db.Integer, db.ForeignKey('character.id')),
    db.Column('ally_id',      db.Integer, db.ForeignKey('character.id'))
)

character_enemy = db.Table('character_enemy',
    db.Column('character_id', db.Integer, db.ForeignKey('character.id')),
    db.Column('enemy_id',     db.Integer, db.ForeignKey('character.id'))
)

character_creator = db.Table('character_creator',
    db.Column('character_id', db.Integer, db.ForeignKey('character.id')),
    db.Column('creator_id'  , db.Integer, db.ForeignKey('person.id'))
)

comic_person = db.Table('comic_person',
    db.Column('comic_id',  db.Integer, db.ForeignKey('comic_issue.id')),
    db.Column('person_id', db.Integer, db.ForeignKey('person.id'))
)

comic_characters = db.Table('comic_characters',
    db.Column('comic_id',     db.Integer, db.ForeignKey('comic_issue.id')),
    db.Column('character_id', db.Integer, db.ForeignKey('character.id'))
)


########
# Models
########


###########
# Character
###########

class Character(db.Model):
    """Represents the character model and pillar for the project.

    Everything from id to origin is a single attribute of a character.

    The rest represents the many to many relationships between other models.

    Note:
        The case with allies and enemies is that they themselves are characters,
        which will reference back to a character model.

    Attributes:
        id (str): id of the character
        name (str): name
        alias (str): other names that the character can go by
        image (str): represents the url of the image in which to display
        description (str): a description of the character
        gender (str): gender of character
        origin (str): Genealogical makeup of the character. i.e. 'alien'
        powers (db.relationship): many to many relationship of the character's powers
        teams  (db.relationship): many to many relationship of the charater's teams
        allies (db.relationship): many to many relationship to the character's allies
        enemies(db.relationship): many to many relationship to the charater's enemies
        creators (db.relationship): many to many relationship to the character's creators
    """
    __tablename__  = 'character'
    __searchable__ = ['name', 'alias', 'description', 'origin']
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(255))
    alias       = db.Column(db.String(255))
    image       = db.Column(db.String(4000))
    description = db.Column(db.String(400000))
    gender      = db.Column(db.String(255))
    origin      = db.Column(db.String(255))
    powers      = db.relationship('Power',                              
                    secondary=character_powers,                         
                    backref=db.backref('characters', lazy='dynamic'))
    teams       = db.relationship('Team',                               
                    secondary=character_team,                           
                    backref=db.backref('characters', lazy='dynamic'))
    allies      = db.relationship('Character',
                    secondary=character_ally,
                    primaryjoin=(character_ally.c.character_id == id),                          
                    secondaryjoin=(character_ally.c.ally_id == id),                           
                    backref=db.backref('allied',     lazy='dynamic'))
    enemies     = db.relationship('Character',
                    secondary=character_enemy,                          
                    primaryjoin=(character_enemy.c.character_id == id),
                    secondaryjoin=(character_enemy.c.enemy_id == id),                         
                    backref=db.backref('enemied',    lazy='dynamic'))
    creators    = db.relationship('Person',                             
                    secondary=character_creator,                        
                    backref=db.backref('characters', lazy='dynamic'))

    def __repr__(self):
        return '<Character %r>' % (self.name)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id' : self.id,
            'name': self.name,
            'alias': self.alias,
            'image': {
                'medium_url': self.image.replace('square_avatar', 'scale_medium'),
                'thumb_url': self.image.replace('square_avatar', 'scale_avatar'),
                'small_url': self.image.replace('square_avatar', 'scale_small')  
            },
            'description': self.description,
            'gender': self.gender,
            'origin': self.origin,
            'powers': self.serialize_many(self.powers),
            'teams': self.serialize_many(self.teams),
            'character_friends': self.serialize_many_characters(self.allies),
            'character_enemies': self.serialize_many_characters(self.enemies),
            'creators': self.serialize_many_characters(self.creators),
            'issue_credits': self.serialize_many_characters(self.comic_issue)
        }

    def serialize_many(self, attr):
        return [ item.serialize for item in attr ]

    def serialize_many_characters(self, attr):
        result = [ item.serialize_clipped for item in attr ]
        print(result)
        return result

    @property
    def serialize_clipped(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': {
                'medium_url': self.image.replace('square_avatar', 'scale_medium'),
                'thumb_url': self.image.replace('square_avatar', 'scale_avatar'),
                'small_url': self.image.replace('square_avatar', 'scale_small')  
            }
        }

###########
# Person
###########

class Person(db.Model):
    """Represents the Person model and pillar for the project.

    Everything from id to gender is a single attribute of a person.

    Note:
        Many to many relationships to comics and to characters are accessible from
        the back references in those classes. SQLAlchemy just generates these for 
        Person automatically.

    Attributes:
        id (str): id of the person
        name (str): name of person
        image (str): represents the url of the image in which to display
        birth_date (DateTime): When the person was born
        country (str): What country to which a person resides
        description (str): What a person does for a living
        website (str): url of the person's personal website
        gender (str): gender of character
    """
    __tablename__  = 'person'
    __searchable__ = ['name', 'description']
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(255))
    image        = db.Column(db.String(4000))
    birth_date   = db.Column(db.DateTime)
    country      = db.Column(db.String(255))
    description  = db.Column(db.String(40000))
    website      = db.Column(db.String(255))
    gender       = db.Column(db.String(255))

    def __repr__(self):
        return '<Person %r>' % (self.name)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': {
                'medium_url': self.image.replace('square_avatar', 'scale_medium'),
                'thumb_url': self.image.replace('square_avatar', 'scale_avatar'),
                'small_url': self.image.replace('square_avatar', 'scale_small')  
            },
            'birth_date': self.birth_date,
            'country': self.country,
            'description': self.description,
            'website': self.website,
            'gender': self.gender,
            #TODO Link issues and Characters here
            'issue_credits': [i.serialize_clipped for i in self.comic_issue],
            'character_credits': [i.serialize_clipped for i in self.creators]
            
        }

    @property
    def serialize_clipped(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': {
                'medium_url': self.image.replace('square_avatar', 'scale_medium'),
                'thumb_url': self.image.replace('square_avatar', 'scale_avatar'),
                'small_url': self.image.replace('square_avatar', 'scale_small')  
            }
        }


##############
# Comic Issue
##############
                   
class Comic_Issue(db.Model):
    """Represents the Comic Issue model and pillar for the project.

    Everything from id to volume_id is a single attribute of an issue.

    Note:
        A comic issue pertains to a single comic book.

    Attributes:
        id (str): id of the comic
        title (str): title of comic
        image (str): represents the url of the image in which to display
        cover_date (DateTime): When the comic was released
        issue_num: issue number within a volume of comics
        description: information about the comic
        volume_id (int): Volume that this issue belongs to
        people (db.relationship): Which people worked on this comic
        characters (db.relationship): Which characters appear in the comic
    """
    __tablename__  = 'comic_issue'
    __searchable__ = ['title', 'description']
    id           = db.Column(db.Integer, primary_key=True)
    title        = db.Column(db.String(255))
    image        = db.Column(db.String(4000))
    cover_date   = db.Column(db.DateTime)
    issue_num    = db.Column(db.Integer)
    description  = db.Column(db.String(4000))
    volume_id    = db.Column(db.Integer, db.ForeignKey('comic_volume.id'))
    people       = db.relationship('Person',                      
                    secondary=comic_person,                             
                    backref=db.backref('comic_issue', lazy='dynamic')) 
    characters   = db.relationship('Character', 
                    secondary=comic_characters, 
                    backref=db.backref('comic_issue', lazy='dynamic'))

    def __repr__(self):
        return '<Comic Issue %r>' % (self.title)

    @property
    def serialize_clipped(self):
        return {
            'id': self.id,
            'name': self.title,
            'image': {
                'medium_url': self.image.replace('square_avatar', 'scale_medium'),
                'thumb_url': self.image.replace('square_avatar', 'scale_avatar'),
                'small_url': self.image.replace('square_avatar', 'scale_small')  
            }
        }

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.title,
            'image': {
                'medium_url': self.image.replace('square_avatar', 'scale_medium'),
                'thumb_url': self.image.replace('square_avatar', 'scale_avatar'),
                'small_url': self.image.replace('square_avatar', 'scale_small')  
            },
            'cover_date': self.cover_date,
            'issue_num': self.issue_num,
            'description': self.description,
            'volume_id': self.volume_id,
            'person_credits' : [i.serialize_clipped for i in self.people],
            'character_credits': [i.serialize_clipped for i in self.characters]
        }

##############
# Comic Volume
##############
                   
class Comic_Volume(db.Model):
    """Represents the Comic Volume model and pillar for the project.

    Everything from id to publisher_id is a single attribute of a person.

    Note:
        A comic volume refers to a collection of comic issues

    Attributes:
        id (str): id of the comic
        title (str): title of comic
        image (str): represents the url of the image in which to display
        launch_date (DateTime): When the comic first launched
        publisher_id (int): What publisher from the publisher table did the publishing
        people (db.relationship): Which people worked on this comic
        characters (db.relationship): Which characters appear in the comic
    """
    __tablename__  = 'comic_volume'
    __searchable__ = ['title', 'description']
    id           = db.Column(db.Integer, primary_key=True)
    title        = db.Column(db.String(255))
    image        = db.Column(db.String(4000))
    num_issues   = db.Column(db.Integer)
    description  = db.Column(db.String(4000))
    launch_year  = db.Column(db.Integer)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))

    def __repr__(self):
        return '<Comic Volume %r>' % (self.title)

###########
# Publisher
###########

class Publisher(db.Model):
    """Represents the publisher model for a certain comic series. This
    is the only model that references this.

    Attributes:
        id (int): id of publisher
        name (str): name of publishing studio
        comic_series (db.relationship) one studio to many comic series relationship
    """
    __tablename__  = 'publisher'
    __searchable__ = ['name', 'description']
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(255))
    image        = db.Column(db.String(4000))
    location_address = db.Column(db.String(400))
    location_city    = db.Column(db.String(400))
    location_state   = db.Column(db.String(400))
    description      = db.Column(db.String(4000))
    comic_volume = db.relationship('Comic_Volume', backref='publisher', lazy='dynamic')

    def __repr__(self):
        return '<Publisher %r>' % (self.name)

#######
# Power
#######

class Power(db.Model):
    """A simple character powers model

    Attributes:
        id (int): id of power
        name (str): name of power
    """
    __tablename__  = 'power'
    __searchable__ = ['name', 'description']
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(255))
    description = db.Column(db.String(4000))

    def __repr__(self):
        return '<Power %r>' % (self.name)

    @property
    def serialize(self, full_data=True):
        return {
            'id': self.id,
            'name': self.name
        }

class Team(db.Model):
    """A simple character powers team

    Attributes:
        id (int): id of team
        name (str): name of team
    """
    __tablename__  = 'team'
    __searchable__ = ['name', 'description']
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(255))
    description = db.Column(db.String(4000))

    def __repr__(self):
        return '<Team %r>' % (self.name)

    @property
    def serialize(self, full_data=True):
        return {
            'id': self.id,
            'name': self.name
        }


