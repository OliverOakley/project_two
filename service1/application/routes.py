from application import app, db 
from application.models import Prizes
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/prizegenerator', methods=['GET','POST'])
def prizegenerator():
    result = requests.get('http://service4:5004/service4').json()
    prize_to_add=Prizes(diceroll= result["dice_roll"], fruit= result["random_fruit"], amount= result["prize"])
    db.session.add(prize_to_add)
    db.session.commit()
    prizes= Prizes.query.order_by(desc("id")).limit(5).all()
    return render_template('prizegenerator.html', prizes=prizes)
