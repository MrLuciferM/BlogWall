# BlogWall/__init__.py

from pickle import FALSE
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)

########################
#### DATABASE SETUP ####
########################

basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tlbajzxrzkwybi:342841bb9449d255eff8f6a694cf56c694bc873214b6fa7ca2e7435be13ff5b1@ec2-3-211-6-217.compute-1.amazonaws.com:5432/d7b8023deinqfu'
app.config['SECRET_KEY'] = 'SOMESECRETKEYIDKWHATTOADDHERE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = FALSE

db = SQLAlchemy(app)
Migrate(app,db)

########################


###### LOGIN CONFIGS ######

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

###########################

#### REGISTERING BLUEPRINTS #########
from BlogWall.core.views import core
from BlogWall.error_pages.handlers import error_pages
from BlogWall.users.views import users
from BlogWall.blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(blog_posts)

#####################################