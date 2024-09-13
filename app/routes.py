

from flask import Blueprint,render_template, jsonify,request

main=Blueprint('main',__name__)


@main.route('/') 
def index():
    title="Home Page of Flask Template"

    return render_template('index.html',title=title)