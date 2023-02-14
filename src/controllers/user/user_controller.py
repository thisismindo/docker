"""User controller
"""
from flask_restful import Resource
from src.services.user.user_service import UserService

USER_SERVICE = UserService()

class UserController(Resource):
  """User controller resource
  """
  def get(self, user_id):
    """Get user record by user_id
    """
    user = USER_SERVICE.get_user(user_id)
    #for demonstration, always return true and static response from
    #user service
    return {'status': True, 'body': user}
