from flask import Blueprint

bp = Blueprint('api', __name__)

from FlaskBlog.ChangeProject.app.api import users, errors, tokens
