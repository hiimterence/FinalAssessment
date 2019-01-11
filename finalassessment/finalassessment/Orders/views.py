from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from finalassessment import generate_client_token, gateway, db
from finalassessment.Orders.model import Orders
import datetime


orders_blueprint = Blueprint(
    'orders', __name__, template_folder='templates')


@orders_blueprint.route("/<medium_id>/new", methods=["GET"])
@login_required
def create(medium_id):
    client_token = generate_client_token()
    return render_template('bids/new.html', medium_id=medium_id, client_token=client_token)


@orders_blueprint.route("<medium_id>/<billboard_id>/checkout", methods=["POST"])
def checkout(medium_id, billboard_id):
    amount = request.form["amount"]
    nonce_from_the_client = request.form["payment_method_nonce"]
    result = gateway.transaction.sale({
        "amount": amount,
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
        }
    })
    if result.is_success:
        new_order = Orders(
            user_id=current_user.id,
            booking_at=datetime.datetime.timestamp(datetime.datetime.now()),
            amount=amount
        )
        db.session.add(new_order)
        db.session.commit()
    else:
        return redirect(url_for('home'))


@orders_blueprint.route("/", methods=["GET"])
def index():
    orders = Orders.query.all()
    return render_template('bids/index.html', orders=orders)
