from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cotizaciones.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)
socketio = SocketIO(app)

# Modelos, rutas y lógica aquí (simplificado para el ZIP)
@app.route('/')
def index():
    return "Cotizador App funcionando"

if __name__ == '__main__':
    socketio.run(app, debug=True)