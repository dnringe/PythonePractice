from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class StudentModel(db.Model):
    __tablename__ = "custaddress"
 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    address = db.Column(db.String())
    pincode = db.Column(db.String())
    country = db.Column(db.String(80)) 
    # email = db.Column(db.String())
    # password = db.Column(db.String()) 
    # gender = db.Column(db.String())  
    # hobbies = db.Column(db.String()) 
    
 
    def __init__(self, first_name,last_name,address,pincode,country):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.pincode = pincode
        self.country = country
        # self.email = email
        # self.password = password
        # self.gender = gender
        # self.hobbies = hobbies
        
 
    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"