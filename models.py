from server import db


############
# M:N Tables
############

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
    db.Column('comic_id',  db.Integer, db.ForeignKey('comic_series.id')),
    db.Column('person_id', db.Integer, db.ForeignKey('person.id'))
)

comic_characters = db.Table('comic_characters',
    db.Column('comic_id',     db.Integer, db.ForeignKey('comic_series.id')),
    db.Column('character_id', db.Integer, db.ForeignKey('character.id'))
)


########
# Models
########

class Character(db.Model):
    __tablename__ = 'character'
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
                'thumb_url': self.image,
                'small_url': self.image.replace('square_avatar', 'scale_small')  
            },
            'description': self.description,
            'gender': self.gender,
            'origin': self.origin,
            'powers': self.serialize_many(self.powers),
            'teams': self.serialize_many(self.teams),
            'character_friends': self.serialize_many_characters(self.allies),
            'character_enemies': self.serialize_many_characters(self.enemies),
            'creators': []
        }

    def serialize_many(self, attr):
        return [ item.serialize for item in attr ]

    def serialize_many_characters(self, attr):
        return [ item.serialize_ally_enemy for item in attr ]

    @property
    def serialize_ally_enemy(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Person(db.Model):
    __tablename__ = 'person'
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(255))
    image        = db.Column(db.String(4000))
    birth_date   = db.Column(db.DateTime)
    country      = db.Column(db.String(255))
    job_title    = db.Column(db.String(255))
    website      = db.Column(db.String(255))
    gender       = db.Column(db.String(255))

    def __repr__(self):
        return '<Person %r>' % (self.name)
                   
class Comic_Series(db.Model):
    __tablename__ = 'comic_series'
    id           = db.Column(db.Integer, primary_key=True)
    title        = db.Column(db.String(255))
    image        = db.Column(db.String(4000))
    launch_date  = db.Column(db.DateTime)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    people       = db.relationship('Person',                      
                    secondary=comic_person,                             
                    backref=db.backref('comic_series', lazy='dynamic')) 
    characters   = db.relationship('Character', 
                    secondary=comic_characters, 
                    backref=db.backref('comic_series', lazy='dynamic'))

    def __repr__(self):
        return '<Comic Series %r>' % (self.title)

class Publisher(db.Model):
    __tablename__ = 'publisher'
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(255))
    comic_series = db.relationship('Comic_Series', backref='publisher', lazy='dynamic')

    def __repr__(self):
        return '<Publisher %r>' % (self.name)

class Power(db.Model):
    __tablename__ = 'power'
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(255))

    def __repr__(self):
        return '<Power %r>' % (self.name)

    @property
    def serialize(self, full_data=True):
        return {
            'id': self.id,
            'name': self.name
        }


class Team(db.Model):
    __tablename__ = 'team'
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(255))

    def __repr__(self):
        return '<Team %r>' % (self.name)

    @property
    def serialize(self, full_data=True):
        return {
            'id': self.id,
            'name': self.name
        }

