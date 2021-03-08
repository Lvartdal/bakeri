from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///butikk.sqlite3'

db = SQLAlchemy(app)


class butikk(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    modell = db.Column('modell', db.String(255))
    pris = db.Column('pris', db.Integer)
    bilde = db.Column('bilde', db.String(255))
    info = db.Column('info', db.String(255))
    relevans = db.Column('relevans', db.Integer)


def __init__(self, pris, bilde, info, relevans, modell):
    self.pris = pris
    self.bilde = bilde
    self.info = info
    self.relevans = relevans
    self.modell = modell


@app.route('/produkter/<sorter>/<rekke>')
def produkter(sorter, rekke):
    butikk = db.engine.execute(
        f'SELECT * FROM butikk ORDER BY "{sorter}" "{rekke}"')
    return render_template('produkter.htmls', butikk=butikk)


@app.route('/')
def index():
    butikk = db.engine.execute(
        'SELECT * FROM butikk')
    return render_template('index.html', butikk=butikk)


app.run(debug=True)
