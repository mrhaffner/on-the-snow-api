from flask import jsonify
from werkzeug.exceptions import abort
from project.models import Resort

def get_resort_by_id(id):
    resort = Resort.query.filter_by(id=id).first()

    if resort is None:
        abort(404, f"Resort id {id} does not exist.")

    return jsonify(Resort.serialize_all(resort))

def get_resort_names_by_state(state):
    resorts = Resort.query.filter_by(state=state).all()

    if resorts is None or len(resorts) == 0:
        abort(404, f"State {state} does not exist or does not have resorts.")

    resortList = [Resort.serialize_name(resort) for resort in resorts]
    resortList.sort(key=lambda resort: resort['id'])
    return jsonify(resortList)

def get_all_resort_names():
    resorts = Resort.query.all()
    resortList = [Resort.serialize_name(resort) for resort in resorts]
    resortList.sort(key=lambda resort: resort['id'])
    return jsonify(resortList)

def get_state_list():
    query = Resort.query.with_entities(Resort.state).distinct()
    return jsonify([state.state for state in query.all()])