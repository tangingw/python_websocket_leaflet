from flask import Flask
from flask import render_template


WEBSOCKET_SERVER = "192.168.43.222"


app = Flask(__name__)


@app.route("/")
def index():
    
    return "Hello World"


@app.route("/location")
def get_oriention():
    
    return render_template("location.html")


@app.route("/location_new")
def get_oriention_new():
    
    return render_template("test_location.html", websocket_ip=WEBSOCKET_SERVER)


@app.route("/location_vue")
def get_orientation_vue():

    return render_template("location_vue.html")


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)