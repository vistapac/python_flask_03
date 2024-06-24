from flask import Flask
import logging
from config import Config
from extensions import db, jwt
from routes import register_blueprints

def create_app():
    app = Flask(__name__)
    # logging.basicConfig(level=logging.DEBUG)
    app.config.from_object(Config)  # 透過 from_object 加載到 Flask 
    
    logging.basicConfig(level=logging.DEBUG)

    db.init_app(app)    #   將 SQLAlchemy 實例與 Flask 應用程式關聯起來
    jwt.init_app(app)
    
    register_blueprints(app)

    with app.app_context():
        db.create_all()

        # 增加新的使用者
        # user = User(username='john', email='john@example.com' , password='john@example.com')
        # db.session.add(user)
        # db.session.commit()

        # print('User added successfully.')



    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
