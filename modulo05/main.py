from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Andre Vitor\\Documents\\repositorios\\Python\\TechTonic\\modulo04\\aplication.sqlite3'
app.config['SECRET_KEY'] = 'moredevs'

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)
