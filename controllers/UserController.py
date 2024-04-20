import sys
from flask import render_template, redirect, url_for, request, abort, jsonify
# from ipdb import ipdb

from models.User import User

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