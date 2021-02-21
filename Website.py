from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "vryencryptedpswrd"

app.permanent_session_lifetime = timedelta(minutes=10)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/multi", methods=["POST", "GET"])
def multiplication():
    if request.method == "POST":
        numonem = request.form["multone"]
        numtwom = request.form["multtwo"]
        return redirect(url_for("calc", result=str(int(numonem) * int(numtwom))))
    else:
        return render_template("times.html")


@app.route("/sub", methods=["POST", "GET"])
def subtraction():
    if request.method == "POST":
        numones = request.form["subone"]
        numtwos = request.form["subtwo"]
        return redirect(url_for("calc", result=str(int(numones) - int(numtwos))))
    else:
        return render_template("sub.html")


@app.route("/add", methods=["POST", "GET"])
def addition():
    if request.method == "POST":
        numonea = request.form["addone"]
        numtwoa = request.form["addtwo"]
        return redirect(url_for("calc", result=str(int(numonea) + int(numtwoa))))
    else:
        return render_template("add.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful!", 'info')
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In", 'info')
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/calc:<result>")
def calc(result):
    return f"<h1>Your Answer is:</h1> <p1>{result}</p1>"


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        flash("You Are Not Logged In!", 'alert')
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You Have Logged Out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


@app.route("/comingsoon")
def comingsoon():
    return render_template('comingsoon.html')


'''@app.route("/<name>")
def usr(name):
    return "hi " + name + "!!!"

@app.route("/lazy")
def lazy():
    return "This is Coming Soon"'''


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
