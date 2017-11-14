from flask import Flask, send_from_directory, render_template, session, request, redirect
app = Flask(__name__)


@app.route("/static/<path:path>")
def static_file(path):
    return send_from_directory("static", path)


@app.route("/")
@app.route("/index.html")
def hello_world():
    if('username' in session):
        return render_template("index.html", user=session["username"])
    return render_template("index.html", user=None)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    success = None
    if(request.method == "POST"):
        if(request.form["pw"] == "mypassword"):
            session["username"] = request.form["un"]
            success = "You are now logged in."
        else:
            error = "Invalid password"
    return render_template("login.html", error=error, success=success)


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/")

@app.errorhandler(404)
def notfound(error):
    return render_template("notfound.html"), 404


app.secret_key = 'e8cb784d05b6'