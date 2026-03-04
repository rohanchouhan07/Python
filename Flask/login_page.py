from flask import Flask,request, redirect,url_for,session,Response
app= Flask(__name__)
app.secret_key= "supersecret"
# home pages
@app.route("/",methods=["GET","POST"])
def login():
    if request.method =="POST":
        username = request.form.get("username")
        password =request.form.get("password")

        if(username=="admin" and password =="123"):
            session["user"]= username
            return redirect(url_for("welcome"))
        else:
            return Response("invalid credentials",mimetype="text/plain")
    
    
    return'''
        <h2>Login foam </h2>
        <form method="POST">
        username: <input type="text" name="username"><br>
        password: <input type="text" name="password"><br>
        <input type="submit" value="Login">
        </form>
'''

# welcome page
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome,{session["user"]}!</h2>
        <a href={url_for('logout')}>Logout</a>
        '''
    return redirect(url_for("login")) #re dirext to the login page again

#logout
@app.route("/logout")
def logout():
    session.pop("user", None) # remove the user
    return redirect(url_for("login"))