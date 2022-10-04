from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    my_list = Flask(__name__)
    my_list.config['SECRET_KEY'] = 'random_secret'
    my_list.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(my_list)

    from .views import views
    from .auth import auth

    my_list.register_blueprint(views, url_prefix='/')
    my_list.register_blueprint(auth, url_prefix='/')

    from .models import User, Note, Event

    create_database(my_list)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(my_list)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return my_list


def create_database(create_this):
    if not path.exists('my_app/' + DB_NAME):
        db.create_all(app=create_this)
        print('Created Database!')
