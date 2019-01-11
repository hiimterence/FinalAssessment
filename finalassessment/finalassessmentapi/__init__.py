from finalassessment import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##
from finalassessmentapi.blueprints.users.views import users_api_blueprint
from finalassessmentapi.blueprints.sessions.views import sessions_api_blueprint
from finalassessmentapi.blueprints.Maids.views import maids_api_blueprint
from finalassessmentapi.blueprints.Orders.views import orders_api_blueprint

app.register_blueprint(sessions_api_blueprint, url_prefix='/api/v1/')
app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(maids_api_blueprint, url_prefix='/api/v1/maids')
app.register_blueprint(orders_api_blueprint, url_prefix='/api/v1/orders')
