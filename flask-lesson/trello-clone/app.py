from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:password123@127.0.0.1:5432/trello'

db = SQLAlchemy(app)

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    title =db.Column(db.String(100))
    desription = db.Column(db.Text())
    date_created = db.Column(db.Date())

@app.cli.command('db_create')
def db_create():
    db.drop_all()
    print("Tables dropped")
    db.create_all()
    print ('Created Tables')

@app.cli.command('db_seed')
def db_seed():
    card1 = Card(
        title = 'Start the project',
        desription = 'Stage 1 - Creation ERD',
        date_created = date.today()
    )
    db.session.add(card1)

    card2 =Card(
        title = 'SQLAlchemy and Marshmallow',
        description = 'Stage 2, integrate both modules in the project',
        status = "ongoing",
        priority ="high",
        date = date.today()
    )
    db.session.add(card2)
    
    db.session.commit()
    print('Database seeded')

@app.route('/')
def index():
    return 'Hello, world'

