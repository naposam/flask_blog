import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '1ee75837a71df28fd91c4449f19b9b0e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manger = LoginManager(app)
login_manger.login_view = 'login'
login_manger.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('ultdev2019@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('ult_devfn@2019')
mail = Mail(app)

from flaskblog import routes