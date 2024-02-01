from FlaskBlog.ChangeProject.app.api import bp
from FlaskBlog.ChangeProject.app.api.auth import basic_auth, token_auth
from FlaskBlog.ChangeProject.app import db


@bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = basic_auth.current_user().get_token()
    db.session.commit()
    return {'token': token}


@bp.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    token_auth.current_user().revoke_token()
    db.session.commit()
    return '', 204
