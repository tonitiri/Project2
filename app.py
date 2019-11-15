from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from mongoengine.connection import connect
import os
import jinja2


# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config['MONGO_DBNAME'] = 'Project2'
mongo = PyMongo(app, uri="mongodb://localhost:27017/Project2")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Find one record of data from the mongo database
    Project2 = mongo.db.Project2.find({})

    # Return template and data
    return render_template('index.html', Project2 = Project2)

# Route to render TEC.html template using data from Mongo
@app.route("/TEC.html")
def TEC():
    # Find one record of data from the mongo database
    TotalEnergyConsumption = mongo.db.TotalEnergyConsumption.find({})


    # Return template and data
    return render_template('TEC.html', TotalEnergyConsumption = TotalEnergyConsumption)

# Route to render TEP.html template using data from Mongo
@app.route("/TEP.html")
def TEP():
    # Find one record of data from the mongo database
    TotalEnergyProduction = mongo.db.TotalEnergyProduction.find({})


    # Return template and data
    return render_template('TEP.html', TotalEnergyProduction = TotalEnergyProduction)

# Route to render EBOT.html template using data from Mongo
@app.route("/EBOT.html")
def EBOT():
    # Find one record of data from the mongo database
    EnergyBalanceOfTrade = mongo.db.EnergyBalanceOfTrade.find({})


    # Return template and data
    return render_template('EBOT.html', EnergyBalanceOfTrade = EnergyBalanceOfTrade)

# Route to render EIG.html template using data from Mongo
@app.route("/EIG.html")
def EIG():
    # Find one record of data from the mongo database
    EnergyIntensityGDP = mongo.db.EnergyIntensityGDP.find({})


    # Return template and data
    return render_template('EIG.html', EnergyIntensityGDP = EnergyIntensityGDP)

# Route to render CC.html template using data from Mongo
@app.route("/CC.html")
def CC():
    # Find one record of data from the mongo database
    coordinates = mongo.db.coordinates.find({})


    # Return template and data
    return render_template('CC.html', coordinates = coordinates)

if __name__ == "__main__":
    app.run()

