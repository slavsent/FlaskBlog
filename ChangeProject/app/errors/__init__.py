from flask import Blueprint

bp = Blueprint('errors', __name__)

from FlaskBlog.ChangeProject.app.errors import handlers
