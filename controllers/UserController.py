import sys
from flask import render_template, redirect, url_for, request, abort, jsonify

from models.User import User

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def index():
    return jsonify({"category": 'category'})

def store():
    return ''

def show(userId):
    return ''

def update(userId):
    return ''

def delete(userId):
    return ''

def destroy(userId):
    ...