from flask_pymongo import PyMongo
from flask import Flask

app = Flask(__name__)


app.config['MONGO_URI'] = 'mongodb://database/apiresmangodb'
mongo = PyMongo(app)