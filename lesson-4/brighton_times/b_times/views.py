from flask import render_template
from b_times import app

@app.route('/')
def index():
    return 'Hello world'