from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)
# Your database should represent a zoo. 
# There should be three tables: animals, zookeepers, and enclosures

# The Zookeeper model should contain a name, a birthday, 
# and a list of animals that they take care of
class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.Date)

    animals = db.relationship('Animal', back_populates='zookeeper')




# The Enclosure model should contain an environment 
# (grass, sand, or water), an open_to_visitors boolean, 
# and a list of animals
class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    # environment = ['grass', 'sand', 'water']
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    animals = db.relationship('Animal', back_populates='enclosure')

# The Animal model should contain a name, a species, 
# a zookeeper, and an enclosure
class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    
    zookeeper = db.relationship('Zookeeper', back_populates='animals')
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))

    enclosure = db.relationship('Enclosure', back_populates='animals')
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))
