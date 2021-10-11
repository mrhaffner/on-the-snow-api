from flask import Blueprint, jsonify
import resort_controller


blueprint = Blueprint('api', __name__, url_prefix='/')

@blueprint.route("/resorts", methods=["GET"])
def get_all_resort_names():
    resorts = resort_controller.get_all_resort_names()
    return jsonify(resorts)

@blueprint.route("/resort/<id>", methods=["GET"])
def get_resort_by_id(id):
    resort = resort_controller.get_resort_by_id(id)
    return jsonify(resort)

@blueprint.route("/resort/state/<state>", methods=["GET"])
def get_resort_names_by_state(state):
    resorts = resort_controller.get_resort_names_by_state(state)
    return jsonify(resorts)