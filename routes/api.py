from flask import Blueprint

# from controllers.UserController import index, store, show, update, destroy
from controllers.UserController import UserController
from controllers.TrainingDataController import TrainingDataController

api = Blueprint('api', __name__)

userController = UserController()
trainingDataController = TrainingDataController()

api.route('users/', methods=['GET'], endpoint='user_index')(userController.index)
api.route('users/create', methods=['POST'], endpoint='user_store')(userController.store)
api.route('users/<int:id>', methods=['GET'], endpoint='user_show')(userController.show)
api.route('users/<int:id>/edit', methods=['POST'], endpoint='user_update')(userController.update)
api.route('users/<int:id>', methods=['DELETE'], endpoint='user_destroy')(userController.destroy)

api.route('training-data/', methods=['GET'], endpoint='td_index')(trainingDataController.index)
# api.route('training-data/create', methods=['POST'])(trainingDataController.store)
# api.route('training-data/<int:id>', methods=['POST'])(trainingDataController.show)