from os import stat
from flask import Flask,render_template,request,session,redirect,url_for
import database as db
import datetime
import random

app = Flask(__name__)
app.secret_key = "12345678"

@app.route("/")
def index():
    print(session.get("user"))
    if session.get("user"):
        if session['user'][3] == "user":
            status = request.args.get("status",0)
            departments = db.getDept()
            return render_template("user/home.html",user=session['user'],status=status,departments=departments)
        else:
            complaints = db.getComplaint()
            print(complaints)
            return render_template("admin/home.html",complaints=complaints)

    status = request.args.get("status",0)
    return render_template("index.html",status=status)

@app.route("/complaint", methods=['POST'])
def complaint():
    user_id = session['user'][0]
    description = request.form['description']
    dept_id = request.form['department']
    today = str(datetime.date.today())
    cid = random.randint(0,1000000000000)
    status = db.addComplaint(cid,user_id,dept_id,description,today)
    return redirect(url_for("index",status=status))

@app.route("/login",methods=["POST"])
def login():
        phone = request.form['phone']
        password = request.form['password']
        user = db.getUser(phone,password)    
        if user:
            session['user'] = user[0]
        return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
        
@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        name=request.form['username']
        phone = request.form['phone']
        password = request.form['password']
        status = db.addUser(name,phone,password)
        return redirect(url_for("index",status=status))
        # return render_template("register.html",status=status)

app.run(debug=True)