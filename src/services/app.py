from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://waldo:1234@postgres/waldo"
db = SQLAlchemy(app)


if __name__ == '__main__':

    from web import *
  
    app.run(host='0.0.0.0', port=3000)