from app import *

@app.route("/")
def index():
    return jsonify(success=True)
