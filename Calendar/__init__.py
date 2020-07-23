"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "hgys8645fsrw2710skjg8762nmal0176aloq3710gtfn2739"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
login_manager = LoginManager(app)
db = SQLAlchemy(app)

import Calendar.views
