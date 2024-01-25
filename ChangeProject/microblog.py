from FlaskBlog.ChangeProject.app import create_app  #, db
from FlaskBlog.ChangeProject.app.models import User, Post, Notification, Message, Task


app = create_app()
#cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification, 'Task': Task}
