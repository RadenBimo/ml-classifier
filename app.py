from flask import Flask, render_template, jsonify
from flask_migrate import Migrate

from models.User import db
from routes.api import api

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return jsonify({"lala": 'lala'})

if __name__ == '__main__':
    app.debug = True
    app.run()