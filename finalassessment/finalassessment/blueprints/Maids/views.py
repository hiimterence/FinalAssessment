from flask import jsonify, Blueprint, request, make_response
from finalassessment.blueprints.Maids.model import Maids
import simplejson as json

maids_api_blueprint = Blueprint('maids_api',
                                __name__,
                                template_folder='templates')


@maids_api_blueprint.route('/maids', methods=['GET'])
def index():
    maids = Maids.query.all()

    all_maids = []
    for maid in maids:
        del maid.__dict__['_sa_instance_state']
        all_maids.append(maid.__dict__)
    

    responseObject = {
        'status': 'success',
        'message': 'All maids returned',
        'all_maids': all_maids
    }

    return make_response(json.dumps(responseObject)), 201
