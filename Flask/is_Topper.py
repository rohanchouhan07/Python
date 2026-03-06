from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def student():
    return render_template("profile.html",
                           name="rohan",
                           is_topper=True,
                           subject=["mahts","science","english"])