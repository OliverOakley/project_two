from application import app, db

class Prizes(db.Model):
    __tablename__ = "Prizes"
    id = db.Column(db.Integer, primary_key=True)
    diceroll = db.Column(db.String(30), nullable=False)
    fruit = db.Column(db.String(30), nullable=False)
    amount = db.Column(db.String(30), nullable=False)