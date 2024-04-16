from flask import Flask, render_template, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import json
from pprint import pformat


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

from routes.api import api

app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return jsonify({"lala": 'lala'})

@app.route('/endpoint', methods=['POST'])
def endpoint_handler():
   
    print(request.headers)
    pretty_json = json.dumps(request.get_json(), indent=4)
    print(pretty_json)
    return jsonify({"data": 'data'})
    # Continue with your logic...


if __name__ == '__main__':
    app.debug = True
    app.run()