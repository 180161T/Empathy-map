from flask import *
from persistence import *
import functools
from his import Hist
from todo import Todo

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)
Hist = Hist()
Todo = Todo()


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

#Xavier Part


@app.route('/')
def main():
     if 'id' in session:
         return render_template('Main Page.html')
     else:
         return render_template('Login_Page.html')


@app.route("/login", methods=['GET', 'POST'])
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
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            create_user(username, password)
            return redirect(url_for('login'))
        flash(error)
    return render_template('Register.html')


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


@app.route("/Aircon", methods=("GET", "POST"))
def aircon():
    return render_template("AirconDesign.html", value=24)


@app.route("/Aircon/increase/<int:value>")
def increase(value):
    if value < 30:
        value = value + 1
        return render_template('AirconDesign.html', value=value)
    else:
        return render_template('AirconDesign.html', value=30)

@app.route("/Aircon/decrease/<int:value>")
def decrease(value):
    if value > 16:
        value = value - 1
        return render_template('AirconDesign.html', value=value)
    else:
        return render_template('AirconDesign.html', value=16)

#Yusuf part


@app.route("/Lighting")
def lighting():
    return render_template("Lighting-control.html")

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


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.debug = True
    app.run()
