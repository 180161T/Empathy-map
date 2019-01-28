from flask import Flask, render_template, request
from Persistence import *
from his import Hist
from CCTV_Persistence import  *

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


@app.route("/CCTV_1", methods=['POST', 'GET'])
def cctv1():
    selected1_0 = ''
    selected1_1 = ''
    selected1_2 = ''
    selected1_3 = ''
    selected1_4 = ''
    selected1_5 = ''
    selected1_6 = ''
    selected1_7 = ''
    selected1_8 = ''
    selected1_9 = ''
    selected1_10 = ''
    selected1_11 = ''
    selected1_12 = ''
    selected1_13 = ''
    selected1_14 = ''
    selected1_15 = ''
    selected1_16 = ''
    selected1_17 = ''
    selected1_18 = ''
    selected1_19 = ''
    selected1_20 = ''
    selected1_21 = ''
    selected1_22 = ''
    selected1_23 = ''

    dateTime1 = getCCTVsetting1('tempUserId')
    if dateTime1 == '0':
        selected1_0 = 'selected'
    elif dateTime1 == '1':
        selected1_1 = 'selected'
    elif dateTime1 == '2':
        selected1_2 = 'selected'
    elif dateTime1 == '3':
        selected1_3 = 'selected'
    elif dateTime1 == '4':
        selected1_4 = 'selected'
    elif dateTime1 == '5':
        selected1_5 = 'selected'
    elif dateTime1 == '6':
        selected1_6 = 'selected'
    elif dateTime1 == '7':
        selected1_7 = 'selected'
    elif dateTime1 == '8':
        selected1_8 = 'selected'
    elif dateTime1 == '9':
        selected1_9 = 'selected'
    elif dateTime1 == '10':
        selected1_10 = 'selected'
    elif dateTime1 == '11':
        selected1_11 = 'selected'
    elif dateTime1 == '12':
        selected1_12 = 'selected'
    elif dateTime1 == '13':
        selected1_13 = 'selected'
    elif dateTime1 == '14':
        selected1_14 = 'selected'
    elif dateTime1 == '15':
        selected1_15 = 'selected'
    elif dateTime1 == '16':
        selected1_16 = 'selected'
    elif dateTime1 == '17':
        selected1_17 = 'selected'
    elif dateTime1 == '18':
        selected1_18 = 'selected'
    elif dateTime1 == '19':
        selected1_19 = 'selected'
    elif dateTime1 == '20':
        selected1_20 = 'selected'
    elif dateTime1 == '21':
        selected1_21 = 'selected'
    elif dateTime1 == '22':
        selected1_22 = 'selected'
    elif dateTime1 == '23':
        selected1_23 = 'selected'

    if request.method == 'POST':
        if 'DateTime1' in request.form:
            dateTime1 = request.form['DateTime1']
            saveCCTVsetting1('tempUserId', dateTime1)

        if 'DateTime2' in request.form:
            date1 = request.form['DateTime2']
            print(date1)

    return render_template("CCTV_1.html", selected1_0=selected1_0, selected1_1=selected1_1, selected1_2=selected1_2,
                           selected1_3=selected1_3, selected1_4=selected1_4, selected1_5=selected1_5,
                           selected1_6=selected1_6, selected1_7=selected1_7, selected1_8=selected1_8,
                           selected1_9=selected1_9, selected1_10=selected1_10,selected1_11=selected1_11,
                           selected1_12=selected1_12, selected1_13=selected1_13, selected1_14=selected1_14,
                           selected1_15=selected1_15, selected1_16=selected1_16, selected1_17=selected1_17,
                           selected1_18=selected1_18, selected1_19=selected1_19, selected1_20=selected1_20,
                           selected1_21=selected1_21, selected1_22=selected1_22, selected1_23=selected1_23)

    selected2_0 = ''
    selected2_1 = ''
    selected2_2 = ''
    selected2_3 = ''
    selected2_4 = ''
    selected2_5 = ''
    selected2_6 = ''
    selected2_7 = ''
    selected2_8 = ''
    selected2_9 = ''
    selected2_10 = ''
    selected2_11 = ''
    selected2_12 = ''
    selected2_13 = ''
    selected2_14 = ''
    selected2_15 = ''
    selected2_16 = ''
    selected2_17 = ''
    selected2_18 = ''
    selected2_19 = ''
    selected2_20 = ''
    selected2_21 = ''
    selected2_22 = ''
    selected2_23 = ''

    dateTime2 = getCCTVsetting1('tempUserId')
    if dateTime2 == '0':
        selected2_0 = 'selected'
    elif dateTime2 == '1':
        selected2_1 = 'selected'
    elif dateTime2 == '2':
        selected2_2 = 'selected'
    elif dateTime2 == '3':
        selected2_3 = 'selected'
    elif dateTime2 == '4':
        selected2_4 = 'selected'
    elif dateTime2 == '5':
        selected2_5 = 'selected'
    elif dateTime2 == '6':
        selected2_6 = 'selected'
    elif dateTime2 == '7':
        selected2_7 = 'selected'
    elif dateTime2 == '8':
        selected2_8 = 'selected'
    elif dateTime2 == '9':
        selected2_9 = 'selected'
    elif dateTime2 == '10':
        selected2_10 = 'selected'
    elif dateTime2 == '11':
        selected2_11 = 'selected'
    elif dateTime2 == '12':
        selected2_12 = 'selected'
    elif dateTime2 == '13':
        selected2_13 = 'selected'
    elif dateTime2 == '14':
        selected2_14 = 'selected'
    elif dateTime2 == '15':
        selected2_15 = 'selected'
    elif dateTime2 == '16':
        selected2_16 = 'selected'
    elif dateTime2 == '17':
        selected2_17 = 'selected'
    elif dateTime2 == '18':
        selected2_18 = 'selected'
    elif dateTime2 == '19':
        selected2_19 = 'selected'
    elif dateTime2 == '20':
        selected2_20 = 'selected'
    elif dateTime2 == '21':
        selected2_21 = 'selected'
    elif dateTime2 == '22':
        selected2_22 = 'selected'
    elif dateTime2 == '23':
        selected2_23 = 'selected'

    if request.method == 'POST':
        if 'DateTime1' in request.form:
            dateTime1 = request.form['DateTime1']
            saveCCTVsetting1('tempUserId', dateTime1)

        if 'DateTime2' in request.form:
            date1 = request.form['DateTime2']
            print(date1)

    return render_template("CCTV_1.html", selected2_0=selected2_0, selected2_1=selected2_1, selected2_2=selected2_2,
                           selected2_3=selected2_3, selected2_4=selected2_4, selected2_5=selected2_5,
                           selected2_6=selected2_6, selected2_7=selected2_7, selected2_8=selected2_8,
                           selected2_9=selected2_9, selected2_10=selected2_10, selected2_11=selected2_11,
                           selected2_12=selected2_12, selected2_13=selected2_13, selected2_14=selected2_14,
                           selected2_15=selected2_15, selected2_16=selected2_16, selected2_17=selected2_17,
                           selected2_18=selected2_18, selected2_19=selected2_19, selected2_20=selected2_20,
                           selected2_21=selected2_21, selected2_22=selected2_22, selected2_23=selected2_23)


@app.route("/CCTV_2", methods=['POST', 'GET'])
def cctv2():
    return render_template("CCTV_2.html")


@app.route("/CCTV_3", methods=['POST', 'GET'])
def cctv3():
    return render_template("CCTV_3.html")


@app.route("/CCTV_4", methods=['POST', 'GET'])
def cctv4():
    return render_template("CCTV_4.html")


@app.route("/View1")
def view1():
    return render_template("View_1.html")


@app.route("/View2")
def view2():
    return render_template("View_2.html")


@app.route("/View3")
def view3():
    return render_template("View_3.html")


@app.route("/View4")
def view4():
    return render_template("View_4.html")


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


if __name__ == "__main__":
    app.run()

