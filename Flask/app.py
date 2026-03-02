from flask import Flask ,request

app= Flask(__name__)

@app.route("/")
def home():
    return 'hello user this is my first flask app'

@app.route("/about")
def about():
    return 'this is about page'

@app.route("/contact")
def contact():
    return 'this is contact ! page'


@app.route("/setting")
def setting():
    return 'this is setting page'

@app.route("/submit",methods=["GET","POST"])
def submit():
    if(request.method=="POST"):
        return "you are send datat"
    else:
        return"you are view"