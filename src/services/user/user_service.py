"""User Service
"""
class UserService:
  def get_user(self, user_id):
    return {
      'user': {
          'id': user_id
      }
    }
