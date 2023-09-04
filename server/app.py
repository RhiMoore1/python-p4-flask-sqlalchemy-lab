#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
# You will need to direct your Flask app to a database at app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# We have imported the Migrate class here to set up our migrations 
# using our Flask application instance and our SQLAlchemy instance.
migrate = Migrate(app, db)
# flask db init has already been run
# We also initialized our application for use within our database
# configuration with db.init_app(app)
db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

# /Flask application in app.py has a resource available at "/animal/<id>"
# /Flask application in app.py displays attributes in animal route in <ul> tags called Name, Species.
# /Flask application in app.py displays attributes in animal route in <ul> tags called Zookeeper, Enclosure.
@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()

    response_body = f''''
    <ul>ID: {animal.id}</ul>',
    <ul>Name: {animal.name}</ul>',
    <ul>Species: {animal.species}</ul>',
    <ul>Zookeeper: {animal.zookeeper.name}</ul>',
    <ul>Enclosure: {animal.enclosure.environment}</ul>'
    '''
    return make_response(response_body)


# /Flask application in app.py has a resource available at "/zookeeper/<id>"
# /Flask application in app.py displays attributes in zookeeper route in <ul> tags called Name, Birthday.
# /Flask application in app.py displays attributes in zookeeper route in <ul> tags called Animal.
# 
@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()

    animals = zookeeper.animals

    response_body = f''''
    <ul>ID: {zookeeper.id}</ul>',
    <ul>Name: {zookeeper.name}</ul>',
    <ul>Birthday: {zookeeper.birthday}</ul>'
    
    '''

    for animal in animals:
        response_body += (f'<ul>Animal: {animal.name}</ul>')


    return make_response(response_body)



# /Flask application in app.py has a resource available at "/enclosure/<id>" 
# /Flask application in app.py displays attributes in enclosure route in <ul> tags called Environment, Open to Visitors.
# /Flask application in app.py displays attributes in enclosure route in <ul> tags called Animal.
# 

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()

    animals = enclosure.animals

    response_body = f''''
    <ul>ID: {enclosure.id}</ul>',
    <ul>Environment: {enclosure.environment}</ul>',
    <ul>Open to Visitors: {enclosure.open_to_visitors}</ul>'
    
    '''
    for animal in animals:
        response_body += (f'<ul>Animal: {animal.name}</ul>')

    return make_response(response_body)



if __name__ == '__main__':
    app.run(port=5555, debug=True)
