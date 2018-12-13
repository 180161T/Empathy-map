# app.secret_key = 'secretkeyhereplease'
from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user
# from .forms import SignupForm
# from .models import db

app = Flask(__name__)
# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UserStorage.db'
#
# login_manager = LoginManager()
# login_manager.init_app(app)
#
#
# @login_manager.user_loader
# def load_user(username):
#     return User.query.filter_by(username=username).first()
#
# @app.route('/protected')
# @login_required
# def protected():
#     return "protected area"

@app.route("/")
def main():
    return render_template("Main Page.html")


@app.route("/login", methods=('GET', 'POST'))
def login():
    # form = SignupForm()
    # if request.method == 'GET':
    #     return render_template('Login_Page.html', form=form)
    # elif request.method == 'POST':
    #     if form.validate_on_submit():
    #         user=User.query.filter_by(username=form.username.data).first()
    #         if user:
    #             if user.password == form.password.data:
    #                 login_user(user)
    #                 return "User logged in"
    #             else:
    #                 return "Wrong password"
    #         else:
    #             return "user doesn't exist"
    # else:
    #         return "form not validated"
    return render_template("Login_Page.html")


@app.route("/register", methods=('GET', 'POST'))
def register():
    # form = SignupForm()
    # if request.method == 'GET':
    #     return render_template('Register.html', form=form)
    # elif request.method == 'POST':
    #     if form.validate_on_submit():
    #         if User.query.filter_by(username=form.username.data).first():
    #             return "Username already exists"
    #         else:
    #             newuser = User(form.username.data, form.password.data)
    #             db.session.add(newuser)
    #             db.session.commit()
    #
    #             login_user(newuser)
    #
    #             return "User created!!!"
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


@app.route("/Aircon")
def aircon():
    return render_template("AirconDesign.html")


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
    return render_template('history.html')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out"

if __name__ == "__main__":
    # app.init_db()
    app.run()

