from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def foam():
    return render_template("foam.html")

@app.route("/submit",methods=["POST"])
def home():
    username=request.form.get("username")
    password=request.form.get("password")

    # if(username=="Rohan" and password == "rohan0795"):
    #     return render_template("welcome.html",name=username)
    value_user={
        'admin':'123',
        'rohan':'rohan07',
        'divya':'2312',
    }
    if username in value_user and password == value_user[username]:
        return render_template("welcome.html",name=username)
    else:
        return "Invalid credentials Try again !!"