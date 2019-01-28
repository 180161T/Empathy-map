from flask import Flask, render_template, request
from persistence import *
import functools

from todo import Todo
import persistence
import datetime
from CCTV_Persistence import *
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

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


# Ryan part
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

# Yusuf part


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

# Kah Ming part


@app.route('/tracker')
def index():
    return render_template('tracker.html')


@app.route('/items')
def items():
    klist = list(Shelveopen.keys())
    if len(klist) > 0:
        for key in klist:
            if key == "Key":
                Result = Shelveopen["Key"]
                Lastest = int(len(Result)) - 1
                r1 = Result

                return render_template('items.html', r1=r1)
        else:
            return render_template('items.html')
    else:
        return render_template('items.html')

@app.route('/Calculation', methods=['GET', 'POST'])
def Adding():

    if request.method == 'POST':
        if 'deleteItem' in request.form:
            deleteItem = request.form['deleteItem']

            if len(deleteItem) != 0:
                deleteIndex = int(deleteItem) - 1
                Value = Shelveopen["Key"]
                Value.pop(deleteIndex)
                del Shelveopen["Key"]
                Shelveopen["Key"] = Value

        if 'AddItems' in request.form:
            Inputss = request.form['AddItems']

            if len(Inputss) != 0:
                klist = list(Shelveopen.keys())
                if len(klist)>0:
                    for key in klist:
                        Check = True
                        if key == "Key":
                            Value = Shelveopen["Key"]
                            Value.append(Inputss)
                            del Shelveopen["Key"]
                            Shelveopen["Key"] = Value
                            Check = False
                    if Check == True:
                        Value = []
                        Value.append(Inputss)
                        Shelveopen["Key"] = Value
                else:
                    Value = []
                    Value.append(Inputss)
                    Shelveopen["Key"] = Value

    return redirect(url_for('items'))




@app.route('/history')
def history():
    alist = list(Shelveopen.keys())
    if len(alist) > 0:
        Value = Shelveopen["Key"]

    now = datetime.datetime.now()

    time = (now.strftime("%Y/%m/%d %H:%M:%S"))

    return render_template('history.html', v=Value, t=time)






@app.route('/map')
def map():




    return render_template('map.html')


if __name__ == '__main__':
    app.debug = True
    app.run()


# Royce part


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

        if 'DateTime1' in request.form:
            date1 = request.form['DateTime1']
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

    dateTime2 = getCCTVsetting1('tempUserId2')
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
        if 'DateTime2' in request.form:
            dateTime2 = request.form['DateTime1']
            saveCCTVsetting1('tempUserId2', dateTime2)

        if 'DateTime2' in request.form:
            date2 = request.form['DateTime2']
            print(date2)

    return render_template("CCTV_1.html", selected2_0=selected2_0, selected2_1=selected2_1, selected2_2=selected2_2,
                           selected2_3=selected2_3, selected2_4=selected2_4, selected2_5=selected2_5,
                           selected2_6=selected2_6, selected2_7=selected2_7, selected2_8=selected2_8,
                           selected2_9=selected2_9, selected2_10=selected2_10, selected2_11=selected2_11,
                           selected2_12=selected2_12, selected2_13=selected2_13, selected2_14=selected2_14,
                           selected2_15=selected2_15, selected2_16=selected2_16, selected2_17=selected2_17,
                           selected2_18=selected2_18, selected2_19=selected2_19, selected2_20=selected2_20,
                           selected2_21=selected2_21, selected2_22=selected2_22, selected2_23=selected2_23)

    if dateTime1 > dateTime2:
        dateTime2 = dateTime1
        dateTime2 += 1


@app.route("/CCTV_2", methods=['POST', 'GET'])
def cctv2():
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

        if 'DateTime1' in request.form:
            date1 = request.form['DateTime1']
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

    dateTime2 = getCCTVsetting1('tempUserId2')
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
        if 'DateTime2' in request.form:
            dateTime2 = request.form['DateTime2']
            saveCCTVsetting2('tempUserId2', dateTime2)

        if 'DateTime2' in request.form:
            date2 = request.form['DateTime2']
            print(date2)

    return render_template("CCTV_1.html", selected2_0=selected2_0, selected2_1=selected2_1, selected2_2=selected2_2,
                           selected2_3=selected2_3, selected2_4=selected2_4, selected2_5=selected2_5,
                           selected2_6=selected2_6, selected2_7=selected2_7, selected2_8=selected2_8,
                           selected2_9=selected2_9, selected2_10=selected2_10, selected2_11=selected2_11,
                           selected2_12=selected2_12, selected2_13=selected2_13, selected2_14=selected2_14,
                           selected2_15=selected2_15, selected2_16=selected2_16, selected2_17=selected2_17,
                           selected2_18=selected2_18, selected2_19=selected2_19, selected2_20=selected2_20,
                           selected2_21=selected2_21, selected2_22=selected2_22, selected2_23=selected2_23)


@app.route("/CCTV_3", methods=['POST', 'GET'])
def cctv3():
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

        if 'DateTime1' in request.form:
            date1 = request.form['DateTime1']
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

    dateTime2 = getCCTVsetting1('tempUserId2')
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
        if 'DateTime2' in request.form:
            dateTime2 = request.form['DateTime2']
            saveCCTVsetting2('tempUserId2', dateTime2)

        if 'DateTime2' in request.form:
            date2 = request.form['DateTime2']
            print(date2)

    return render_template("CCTV_1.html", selected2_0=selected2_0, selected2_1=selected2_1, selected2_2=selected2_2,
                           selected2_3=selected2_3, selected2_4=selected2_4, selected2_5=selected2_5,
                           selected2_6=selected2_6, selected2_7=selected2_7, selected2_8=selected2_8,
                           selected2_9=selected2_9, selected2_10=selected2_10, selected2_11=selected2_11,
                           selected2_12=selected2_12, selected2_13=selected2_13, selected2_14=selected2_14,
                           selected2_15=selected2_15, selected2_16=selected2_16, selected2_17=selected2_17,
                           selected2_18=selected2_18, selected2_19=selected2_19, selected2_20=selected2_20,
                           selected2_21=selected2_21, selected2_22=selected2_22, selected2_23=selected2_23)

@app.route("/CCTV_4", methods=['POST', 'GET'])
def cctv4():
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

        if 'DateTime1' in request.form:
            date1 = request.form['DateTime1']
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

    dateTime2 = getCCTVsetting1('tempUserId2')
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
        if 'DateTime2' in request.form:
            dateTime2 = request.form['DateTime2']
            saveCCTVsetting2('tempUserId2', dateTime2)

        if 'DateTime2' in request.form:
            date2 = request.form['DateTime2']
            print(date2)

    return render_template("CCTV_1.html", selected2_0=selected2_0, selected2_1=selected2_1, selected2_2=selected2_2,
                           selected2_3=selected2_3, selected2_4=selected2_4, selected2_5=selected2_5,
                           selected2_6=selected2_6, selected2_7=selected2_7, selected2_8=selected2_8,
                           selected2_9=selected2_9, selected2_10=selected2_10, selected2_11=selected2_11,
                           selected2_12=selected2_12, selected2_13=selected2_13, selected2_14=selected2_14,
                           selected2_15=selected2_15, selected2_16=selected2_16, selected2_17=selected2_17,
                           selected2_18=selected2_18, selected2_19=selected2_19, selected2_20=selected2_20,
                           selected2_21=selected2_21, selected2_22=selected2_22, selected2_23=selected2_23)


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
