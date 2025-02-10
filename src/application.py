from flask import Flask
from flask import render_template
from flask import jsonify


application = Flask(__name__)

@application.route("/")
def index():
    """index route"""
    return render_template("index.html",greeting="Artur")
    #return "Hello World! v1.1"

@application.route("/health")
def health():
    """health route"""
    state = {"status": "UP"}
    return jsonify(state)

# run the app.
if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)


