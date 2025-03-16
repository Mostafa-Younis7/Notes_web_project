from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy()
DB_NAME = 'database.db'
app.config['SECRET_KEY'] = 'lksdjfhgldisaof'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .views import views
from .auth import auth

from .models import User, Note

if not path.exists('C:\\Users\\myou3\\note_book_project\\instance\\' + DB_NAME):
    with app.app_context():
        db.create_all()
        print('database is successfully created!')

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')