from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

#   初始化 SQLAlchemy、JWT
db = SQLAlchemy()
jwt = JWTManager()