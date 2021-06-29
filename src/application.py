from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! v1.1"

# run the app.
if __name__ == "__main__":
    application.run()