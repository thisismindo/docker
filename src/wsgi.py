""" App
"""
import os
from flask import Flask
from flask_restful import Api
from src.constant import VERSION
from src.routes.user.user_route import generate_user_routes

application = Flask(__name__)
application.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024
api = Api(application)

generate_user_routes(api, VERSION)

if __name__ == '__main__':
    application.run(debug=os.environ.get('debugMode'))
