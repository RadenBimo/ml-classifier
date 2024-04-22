import sys, json
from flask import render_template, redirect, url_for, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.TrainingData import TrainingData
from models.ModelProduct import ModelProduct
from services.utils import Utils
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

            db.session.query(TrainingData).filter(TrainingData.client_id == 1).delete()

            # Loop through messages, clean and, save them to database
            for message_data in data.get('data', []):
                # message = TrainingData(
                #     client_id=clientId,
                #     message=DataCleaning(message_data.get('message')).clean(),
                #     category=message_data.get('category'),
                # )
                message = TrainingData(
                    client_id=clientId,
                    message=Utils.dataClean(message_data.get('message')),
                    category=message_data.get('category'),
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

    def train_model(self):
        try:
            # Get JSON data from request body
            data = request.get_json()

            # Extract client ID
            clientId = data.get('client_id')
            productId = data.get('product_id')

            query_result = db.session.query(TrainingData.message,TrainingData.category).filter(TrainingData.product_id == {productId})
            df = pd.read_sql(query_result.statement, query_result.session.bind)
            models , scores = create_model(df)

        # Save model to model library models
            models_path = save_model(clientId,productId,models)
            
        # Loop through models, and save them to database
            for key, model_path in models_path.items():
                message = ModelProduct(
                    client_id=clientId,
                    product_id=productId,
                    model_path=model_path,
                    score=scores.get(key),
                    is_selected=False,
                )
                db.session.add(message)

            return 'model saved successfully!', 201  # Created status code

        except Exception as e:
            return jsonify({"error": str(e)}), 400