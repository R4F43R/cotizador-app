from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class QuoteRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100))
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default="pending")
    signature = db.Column(db.Text, nullable=True)
    attachment_path = db.Column(db.String(200), nullable=True)

class QuoteHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quote_id = db.Column(db.Integer, db.ForeignKey('quote_request.id'))
    action = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)