from app import app
from flask import render_template, url_for


@app.route('/')
def home():
    return render_template('index.html', title='Sohbet Gurbanov')
