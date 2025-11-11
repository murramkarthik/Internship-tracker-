from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Internship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default="Ongoing")
