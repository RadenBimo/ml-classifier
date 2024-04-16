import sys, json
from flask import render_template, redirect, url_for, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.TrainingData import TrainingData
from app import db
# db = SQLAlchemy()
class TrainingDataController:
  
    def index(self):
        return jsonify({"lili": 'lili'})

    def store(self):
        try:
            # Get JSON data from request body
            data = request.get_json()

            # Extract client ID
            clientId = data.get('client_id')

            # Loop through messages and save them to database
            for message_data in data.get('data', []):
                message = TrainingData(
                    client_id=clientId,
                    message=message_data.get('message'),
                    category=message_data.get('category')
                )
                db.session.add(message)

            # Commit changes to database
            db.session.commit()

            return 'Data saved successfully!', 201  # Created status code

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    def show(self):
        return ''

    def update(self):
        return ''

    def delete(self):
        return ''

    def destroy(self):
        return ''