import os
import dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# TODO
# Add a new column "updated_by_user" to the database
# Date column returns to "not a primary key" after db migrate and upgrade


dotenv.load_dotenv()
PGSQL_HOST = os.getenv("PGSQL_HOST")
PGSQL_USER = os.getenv("PGSQL_USER")
PGSQL_PASSWORD = os.getenv("PGSQL_PASSWORD")
PGSQL_DB = os.getenv("PGSQL_DB")
PGSQL_PORT = os.getenv("PGSQL_PORT")
SECRET_KEY = os.getenv("SECRET_KEY")

admin = Admin()
db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    from routes import register_routes
    from models import User, FreshiiData, RestrictedAdminView
    
    app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{PGSQL_USER}:{PGSQL_PASSWORD}@{PGSQL_HOST}:{PGSQL_PORT}/{PGSQL_DB}'

    admin.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    
    
    admin.add_view(RestrictedAdminView(User, db.session, endpoint="user_view"))
    admin.add_view(RestrictedAdminView(FreshiiData, db.session, endpoint="freshii_data_view"))
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # bcrypt = Bcrypt(app)
    
    register_routes(app, db, bcrypt)
    
    migrate = Migrate(app, db)
    return app
