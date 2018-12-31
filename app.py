from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from his import Hist

app = Flask(__name__)
Hist = Hist()

app.config.from_pyfile('app.py')

db = SQLAlchemy(app)

@app.route("/")
def main():
    return render_template("Main Page.html")


@app.route("/login", methods=('GET', 'POST'))
def login():
    return render_template("Login_Page.html")




@app.route("/register", methods=('GET', 'POST'))
def register():
    return render_template("Register.html")




@app.route("/remind")
def reminder():
    return render_template("Reminder page.html")


@app.route("/CCTV")
def cctv():
    return render_template("CCTV.html")


@app.route("/CCTV_1")
def cctv1():
    return render_template("CCTV_1.html")


@app.route("/CCTV_2")
def cctv2():
    return render_template("CCTV_2.html")


@app.route("/CCTV_3")
def cctv3():
    return render_template("CCTV_3.html")


@app.route("/CCTV_4")
def cctv4():
    return render_template("CCTV_4.html")


@app.route("/Aircon", methods=("GET", "POST"))
def aircon():
    return render_template("AirconDesign.html", value=24)

@app.route("/Aircon/update/<int:value>")
def update(value):
    value = value + 1
    return render_template('AirconDesign.html', value=value)

@app.route("/Lighting")
def lighting():
    return render_template("Lighting-control.html")


@app.route('/tracker')
def index():
    return render_template('tracker.html')


@app.route('/items')
def items():
    return render_template('items.html')


@app.route('/history')
def history():
    return render_template('history.html', history=Hist)


@app.route('/map')
def map():
    return render_template('map.html')


@app.route("/logout")
# @login_required
def logout():

    return "Logged out"




if __name__ == "_main_":
    app.run()