from flask import Blueprint

bp = Blueprint('auth', __name__)

from FlaskBlog.ChangeProject.app.auth import routes
