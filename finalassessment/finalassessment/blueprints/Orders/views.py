from flask import jsonify, Blueprint, request, make_response
from finalassessment.blueprints.Orders.model import Orders, db
import simplejson as json
from finalassessment.blueprints.users.model import User
from finalassessment import generate_client_token, gateway
# from finalassessment.helpers.sendgrid import send_bid_email

orders_api_blueprint = Blueprint('orders_api',
                               __name__,
                               template_folder='templates')


@orders_api_blueprint.route('/', methods=['GET'])
def index():
    orders = Orders.query.all()
    all_orders = []
    for bid in orders:
        del bid.__dict__['_sa_instance_state']
        all_orders.append(bid.__dict__)

    return json.dumps(all_orders)


@orders_api_blueprint.route('/new_token', methods=['GET'])
def new_token():
    client_token = generate_client_token()

    return jsonify(client_token)


@orders_api_blueprint.route('/new_order', methods=['POST'])
def new_order():
    # get the post data
    post_data = request.get_json()
    user_id = post_data.get('user_id')
    amount = post_data.get('amount')
    nonce_from_the_client = post_data.get('nonce')
    result = gateway.transaction.sale({
        "amount": amount,
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": False
        }
    })

    if result.is_success:
        new_order = Orders(
            user_id=post_data.get('user_id'),
            # medium_id=post_data.get('medium_id'),
            booking_at=post_data.get('booking_at'),
            amount=amount
        )
        db.session.add(new_order)
        db.session.commit()
        # send_bid_email(User.query.get(user_id).email, new_bid.id)

        responseObject = {
            'status': 'success',
            'message': result.transaction.status,
            'details': f'{result.transaction.processor_response_code} : {result.transaction.processor_response_text}'
        }

        return make_response(jsonify(responseObject)), 201

    else:
        responseObject = {
            'status': ' api success but payment failed',
            'message': result.transaction.status,
            'details': f'{result.transaction.processor_response_code} : {result.transaction.processor_response_text}'
        }

        return make_response(jsonify(responseObject)), 201


@orders_api_blueprint.route('/me', methods=['GET'])
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

