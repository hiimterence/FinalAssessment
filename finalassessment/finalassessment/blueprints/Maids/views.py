from flask import jsonify, Blueprint, request, make_response
from finalassessment.blueprints.Maids.model import Maids
import simplejson as json
from finalassessment import db

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

@maids_api_blueprint.route('/bookmaid', methods=['POST'])
def update():
    post_data = request.get_json()
    print(post_data)
    maidid=post_data.get('id')

    maid = Maids.query.get(maidid)
    
    maid.place_to_meet = post_data.get('place_to_meet')
    maid.scheduled_to_meet = post_data.get('scheduled_to_meet')

    db.session.add(maid)
    db.session.commit()

    responseObject = {
        'status': 'success',
        'message': 'maid booked!',
    }

    return make_response(json.dumps(responseObject)), 201
