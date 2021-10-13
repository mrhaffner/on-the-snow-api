from flask import Blueprint, jsonify
import project.resort_controller as resort_controller


blueprint = Blueprint('api', __name__, url_prefix='/')

@blueprint.route("/resorts", methods=["GET"])
def get_all_resort_names():
    return resort_controller.get_all_resort_names()

@blueprint.route("/resorts/<id>", methods=["GET"])
def get_resort_by_id(id):
    return resort_controller.get_resort_by_id(id)

@blueprint.route("/resorts/states", methods=["GET"])
def get_state_list():
    return resort_controller.get_state_list()

@blueprint.route("/resorts/states/<state>", methods=["GET"])
def get_resort_names_by_state(state):
    return resort_controller.get_resort_names_by_state(state)