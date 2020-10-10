from flask import Flask, render_template  
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from webapp.db import db
from webapp.user.models import User
from flask_migrate import Migrate

from webapp.user.views import blueprint as user_blueprint

from flask_login import UserMixin


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    #миграция базы данных
    migrate = Migrate(app, db)


    #покдючаем LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(user_blueprint)

    #функция получающая при запросе нужного пользователя
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    

    return app
    
if __name__ == "__main__":
    app = create_app()
    app.run()
               


