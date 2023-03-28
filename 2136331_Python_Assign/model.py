from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class CustomerModel(db.Model):
    __tablename__  = "customers"

    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    country = db.Column(db.String())

    def __init__(self, first_name, last_name, email, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.country = country
        