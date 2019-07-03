from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://waldo:1234@postgres/waldo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


if __name__ == '__main__':

  from views.web import *

  app.run(host='0.0.0.0', port=3000)
