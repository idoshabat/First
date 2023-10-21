from flask import Flask, render_template, request, session
import csv
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def hello_worlddd():
    return render_template('home.html')


@app.route('/<string:page_name>')
def hello(page_name):
    return render_template(page_name)
