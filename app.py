from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import resort_controller
from routes import blueprint

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resorts.sqlite3'
db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)

app.register_blueprint(blueprint)

@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == '__main__':
    app.run(debug=True)