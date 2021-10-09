from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import resort_controller

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resorts.sqlite3'
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)


@app.route("/resort/<id>", methods=["GET"])
def get_resort_by_id(id):
    resort = resort_controller.get_resort_by_id(id)
    return jsonify(resort)

@app.route("/resort/state/<state>", methods=["GET"]) #maybe use id instead?
def get_resort_names_by_state(state):
    resorts = resort_controller.get_resort_names_by_state(state)
    return jsonify(resorts)

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == '__main__':
    app.run(debug=True)