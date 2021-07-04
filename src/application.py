from flask import Flask
from flask import render_template
import os

application = Flask(__name__)

@application.route("/")
def hello():
    #print(os.getcwd())
    return render_template("index.html",greeting="Artur")
    #return "Hello World! v1.1"

# run the app.
if __name__ == "__main__":
    application.run()


