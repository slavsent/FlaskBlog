from FlaskBlog.app import app, db, cli
from FlaskBlog.app.models import User, Post



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
