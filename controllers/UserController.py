import sys
from flask import render_template, redirect, url_for, request, abort, jsonify

from models.User import User

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class UserController:
    def index(self):
        return jsonify({"lulu": 'lulu'})

    def store(self):
        return ''

    def show(self):
        return ''

    def update(self):
        return ''

    def delete(self):
        return ''

    def destroy(self):
        return ''