import os
import config
import braintree
import sendgrid
from flask import Flask, render_template, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_assets import Bundle, Environment
from authlib.flask.client import OAuth
from clarifai.rest import ClarifaiApp, Workflow
from clarifai.rest import Image as ClImage
from clarifai.rest import Video as ClVideo

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


# session options parameter is used to override session options. If provided it's a dict of parameters passed to the session's
db = SQLAlchemy(app, session_options={"autoflush": False})
# db = SQLAlchemy(app)

Migrate(app, db)
config = eval((os.environ['APP_SETTINGS']))

# not required with react - login handled on the frontend
login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = "sessions.new"
# login_manager.session_protection = "basic"
# login_manager.login_message = "Please login to bidboard first"


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None

# S3 initialisation and upload setup
S3_BUCKET = config.S3_BUCKET
S3_LOCATION = f'http://{S3_BUCKET}.s3.amazonaws.com/'
S3_KEY = config.S3_KEY
S3_SECRET = config.S3_SECRET



# Sendgrid mailing service setup
# SENDGRID_API_KEY = config.SENDGRID_API_KEY
# sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)


# Braintree Setup & Environment Conditions (Sandbox)
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
from finalassessment.users.model import User
from finalassessment.Maids.model import Maids
from finalassessment.Orders.model import Orders

# Home Page
@app.route("/")
def home():
    if current_user.is_authenticated:
        return render_template('home.html', id=current_user.id)
    else:
        return render_template('home.html')


# Grab the blueprints from the other views.py files for each "app"
# make sure route and method is defined in views.py
from finalassessment.users.views import users_blueprint

from finalassessment.Orders.views import orders_blueprint
import finalassessmentapi

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(orders_blueprint, url_prefix='/bids')



# Flask_Assets
assets = Environment(app)

js = Bundle('js/vendor/jquery_3.2.1.js', 'js/vendor/popper_1.11.0.js', 'js/vendor/bootstrap_4.1.1.js',
            filters='jsmin', output='gen/packed.%(version)s.js')

css = Bundle('css/vendor/bootstrap_4.1.1.css', 'css/style.css',
             filters='cssmin', output='gen/packed.%(version)s.css')

assets.register({'js_all': js, 'css_all': css})
