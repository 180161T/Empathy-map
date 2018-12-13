from flask import Flask, render_template
from his import Hist

app = Flask(__name__)

Hist = Hist()


@app.route("/")
def main():
    return render_template("Main Page.html")


@app.route("/login", methods=('GET', 'POST'))
def login():
    login_form = LoginForm(request.form)
    error = None
    if request.method == 'POST':
        user = get_user(login_form.id.data, login_form.password.data)
        if user is None:
            error = 'Wrong username and password'
        else:
            session['username'] = user.username
            return redirect (url_for('index'))
        flash(error)
    return render_template("Login_Page.html", form=login_form)


@app.route("/register", methods=('GET', 'POST'))
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        username = form.id.data
        password = form.password.data
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            create_user(username, password)
            return redirect (url_for('login'))
        flash(error)
    return render_template("Register.html", form=form)




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




@app.route('/logout')
def logout():
    session.clear()
    return login()

if __name__ == "_main_":
    app.run()