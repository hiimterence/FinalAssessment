from flask_cors import CORS
import os
import config
import braintree
from flask import Flask, render_template, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_assets import Bundle, Environment

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


# session options parameter is used to override session options. If provided it's a dict of parameters passed to the session's
db = SQLAlchemy(app, session_options={"autoflush": False})
# db = SQLAlchemy(app)

Migrate(app, db)
config = eval((os.environ['APP_SETTINGS']))

S3_BUCKET = config.S3_BUCKET
S3_LOCATION = f'http://{S3_BUCKET}.s3.amazonaws.com/'
S3_KEY = config.S3_KEY
S3_SECRET = config.S3_SECRET

BRAINTREE_MERCHANT_ID = config.BRAINTREE_MERCHANT_ID
BRAINTREE_PUBLIC_KEY = config.BRAINTREE_PUBLIC_KEY
BRAINTREE_PRIVATE_KEY = config.BRAINTREE_PRIVATE_KEY

gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=BRAINTREE_MERCHANT_ID,
        public_key=BRAINTREE_PUBLIC_KEY,
        private_key=BRAINTREE_PRIVATE_KEY
    )
)

def generate_client_token():
    return gateway.client_token.generate()


# import user, image & marketplace models so that you can run migration
from finalassessment.blueprints.users.model import User
from finalassessment.blueprints.Maids.model import Maids
from finalassessment.blueprints.Orders.model import Orders

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from finalassessment.blueprints.users.views import users_api_blueprint
from finalassessment.blueprints.sessions.views import sessions_api_blueprint
from finalassessment.blueprints.Maids.views import maids_api_blueprint
from finalassessment.blueprints.Orders.views import orders_api_blueprint

app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users/create')
app.register_blueprint(sessions_api_blueprint, url_prefix='/api/v1/')
app.register_blueprint(maids_api_blueprint, url_prefix='/api/v1/maids')
app.register_blueprint(orders_api_blueprint, url_prefix='/api/v1/orders')
