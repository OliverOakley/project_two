from application import app, db 
from application.models import Prizes, Results
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/prizegenerator', methods=['GET','POST'])
def prizegenerator():
    return render_template('prizegenerator.html')
