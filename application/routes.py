from flask import Flask, Blueprint,render_template
import os

chat = Blueprint('chat', __name__)

@chat.route('/')
@chat.route('/home')
def home():
    return render_template('home.html')
