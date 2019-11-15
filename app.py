from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
# from mongoengine.connection import connect
import os
import jinja2


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config['MONGO_DBNAME'] = 'Project2'
mongo = PyMongo(app, uri="mongodb://localhost:27017/Project2")


# Route to render index.html template using data from Mongo
@app.route("/index.html")
def index():
    # Find one record of data from the mongo database
    Project2 = mongo.db.Project2.find({})

    # Return template and data
    return render_template('index.html', Project2 = Project2)

# Route to render index.html template using data from Mongo
@app.route("/TEC.html")
def TEC():
    # Find one record of data from the mongo database
    TEC = mongo.db.TotalEnergyConsumption.find({})

    # Return template and data
    return render_template('TEC.html', TEC = TEC)

if __name__ == "__main__":
    app.run()