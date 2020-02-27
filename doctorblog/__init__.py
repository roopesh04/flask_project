# doctorblog/__init__.py
import os
from flask import Flask,request,send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_qrcode import QRcode


app = Flask(__name__)
qrcode=QRcode(app)
app.config['SECRET_KEY'] = 'mysecret'


############################
### DATABASE SETUP ##########
########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

#########################
# LOGIN CONFIGS
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'



##################################################


from doctorblog.core.views import core
from doctorblog.users.views import users
from doctorblog.error_pages.handlers import error_pages
from doctorblog.blog_posts.views import posts
from doctorblog.api.send_data import data

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(error_pages)
app.register_blueprint(posts)
app.register_blueprint(data)

@app.route("/qrcode", methods=["GET"])
def get_qrcode():
    data = request.args.get("data", "")
    return send_file(qrcode(url, mode="raw"), mimetype="image/png")