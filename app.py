from flask import *
from persistence import *
import functools
from his import Hist
from todo import Todo
import persistence
import datetime
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)
Hist = Hist()
Todo = Todo()

#Xavier Part


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session['id'] is None:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view


@app.route('/init')
def init():
    init_db()
    return 'db initialised'


@app.route('/')
def main():
    if 'id' in session:
        return render_template('Main Page.html')
    else:
        return render_template('Login_Page.html')


@app.route('/login',  methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = get_user(username, password)
            if user is None:
                error = 'Wrong username and password'
            else:
                session['id'] = user.get_id()
                session['user_name'] = user.get_username()
                return redirect(url_for('main'))
        flash(error)
    return render_template('Login_Page.html')


@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # reenter = request.form['reenter']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        # elif password != reenter:
        #     error = 'Password must be the same'
        else:
            create_user(username, password)
            flash("Thanks for registering!")
            return redirect(url_for('login'))
        flash(error)
    return render_template('Register.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main'))


@app.route("/home")
def home():
    return render_template("Main Page.html")


@app.route("/remind")
def remind():
    return render_template("remind.html", todo=Todo)

#Royce part


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


#Ryan part
TemperatureOpen = shelve.open("Temperature")

@app.route("/Aircon", methods=("GET", "POST"))
def aircon():
    DefaultValue = 24
    klist = list(TemperatureOpen.keys())
    for keys in klist:
        if keys == "Key": #Change to a unique ID later
            DefaultValue = TemperatureOpen[keys]
    return render_template("AirconDesign.html", value=DefaultValue)


@app.route("/Aircon/increase/<int:value>")
def increase(value):
    if value < 30:
        value = value + 1
        Temp = Temperature("Key")
        Temp.setTemperature(value)
        Temp.StoreData()
        return render_template('AirconDesign.html', value=value)
    else:
        return render_template('AirconDesign.html', value=30)


@app.route("/Aircon/decrease/<int:value>")
def decrease(value):
    if value > 16:
        value = value - 1
        Temp = Temperature("Key")
        Temp.setTemperature(value)
        Temp.StoreData()
        return render_template('AirconDesign.html', value=value)
    else:
        return render_template('AirconDesign.html', value=16)

#Yusuf part


@app.route("/Lighting", methods=("GET","POST"))
def lighting():
    if request.method=="POST":
        v=request.form["L1"]
        persistence.createsettings(v)
        print(v)
        v2 = request.form["L2"]
        persistence.createsettings(v2)
        print(v2)
        v3 = request.form["L3"]
        persistence.createsettings(v3)
        print(v3)
        v4 = request.form["L4"]
        persistence.createsettings(v4)
        print(v4)
        return render_template("Lighting-control.html")
    else:
        return render_template("Lighting-control.html")


@app.route("/sah", methods=('GET', 'POST'))
def time_alert():
    if request.method == 'POST':
        time1 = datetime.datetime.now().time().hour
        persistence.addTime('user1', datetime.datetime.now())
        if 7<= datetime.datetime.now().time().hour < 9:
            msg = "Warning, It is still bright out ,save electricity!"
            return render_template("time-alert.html", msgHTML=msg)
        else:
            return render_template("Lighting-control2.html")
    return render_template("time-alert.html")


@app.route('/timehistory')
def time_history():



    timeList = persistence.getTime('user1')
    if timeList == None:
        print("No record")
    else:
        for t in timeList:
            print(t)

    return render_template("timeHistory.html", timeList=timeList)

@app.route("/Lighting2")
def lighting2():
    return render_template("Lighting-control2.html")


@app.route("/Lightsaving")
def savedsettings():
    return render_template("LightSaving.html")



@app.route("/w")
def save_setting():
   return render_template("LightSaving.html")

#Kah Ming part


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


if __name__ == '__main__':
    app.debug = True
    app.run()
