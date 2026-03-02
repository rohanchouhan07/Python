from flask import Flask ,request

app=Flask("__name__")

@app.route("/")
def home():
    return 'hello user this is my first flask app submit???????'

@app.route("/submit",methods=["GET","POST"])
def submit():
    if(request.method=="POST"):
        return "you are send datat"
    else:
        return"you are view"
