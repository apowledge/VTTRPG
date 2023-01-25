"""

"""

import os
import pandas as pd

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcyrpt import Bcrypt
from flask_login import LoginManager
from flask_gravatar import Gravatar

#from VTTRPG.config import Config

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
gravatar = Gravatar(app, size=100, rating='g', default='identicon', force_default=False, use_ssl=False, base_url=None)



