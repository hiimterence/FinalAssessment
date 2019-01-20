from flask import jsonify, Blueprint, request, make_response
from finalassessment.blueprints.users.model import User, db
# from finalassessment.helpers.sendgrid import send_signup_email

users_api_blueprint = Blueprint('users_api',
                                __name__,
                                template_folder='templates')


@users_api_blueprint.route('/', methods=['GET'])
def index():
    users = User.query.all()

    users = [{"id": int(user.id),
              "first_name": user.first_name,  "last_name": user.last_name,"email": user.email} for user in users]

    return jsonify(users)


@users_api_blueprint.route('/create', methods=['POST'])
def create():
    # get the post data
    post_data = request.get_json()
    print(post_data)
    new_user = User(
        first_name=post_data.get('first_name'),
        last_name=post_data.get('last_name'),
        email=post_data.get('email').lower(),
        password=post_data.get('password')
    )

    if len(new_user.validation_errors) > 0:

        responseObject = {
            'status': 'fail',
            'message': new_user.validation_errors
        }

        return make_response(jsonify(responseObject)), 401

    else:
        db.session.add(new_user)
        db.session.commit()
        auth_token = new_user.encode_auth_token(new_user.id)
        del new_user.__dict__['_sa_instance_state']
        del new_user.__dict__['password_hash']
        del new_user.__dict__['validation_errors']

        responseObject = {
            'status': 'success',
            'message': 'Successfully created a user and signed in.',
            'auth_token': auth_token.decode(),
            'user': new_user.__dict__
        }

        return make_response(jsonify(responseObject)), 201


@users_api_blueprint.route('/me', methods=['GET'])
def show():
    auth_header = request.headers.get('Authorization')

    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        responseObject = {
            'status': 'failed',
            'message': 'No authorization header found'
        }

        return make_response(jsonify(responseObject)), 401

    user_id = User.decode_auth_token(auth_token)
    user = User.query.get(user_id)

    if user:
        del user.__dict__['_sa_instance_state']
        del user.__dict__['password_hash']
        return jsonify(user.__dict__)

    else:
        responseObject = {
            'status': 'failed',
            'message': 'Authentication failed'
        }

        return make_response(jsonify(responseObject)), 401
