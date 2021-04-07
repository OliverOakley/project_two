from application import app, db

class Prizes(db.Model):
    __tablename__ = "Prizes"
    id = db.Column(db.Integer, primary_key=True)
    results_id = db.Column('Results_id', db.Integer, db.ForeignKey('Results.id'))
    amount = db.Column(db.String(30), nullable=False)

class Results(db.Model):
    __tablename__ = "Results"
    id = db.Column(db.Integer, primary_key=True)
    results = db.Column(db.String(30), nullable=False)
    Prizes = db.relationship('Prizes', backref='Results')