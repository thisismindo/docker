"""User Route
"""
from src.controllers.user.user_controller import UserController

def generate_user_routes(api, version):
  """Define user's route resources
  """
  api.add_resource(
    UserController,
    f'/api/{version}/user/<string:user_id>',
    endpoint='user_get')
