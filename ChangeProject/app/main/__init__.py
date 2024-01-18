from flask import Blueprint

bp = Blueprint('main', __name__)

from FlaskBlog.ChangeProject.app.main import routes
