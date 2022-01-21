from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


@APP.ROUTE("/sub", methods = ['POST'])
def submit():

    # html -> .py
    if request.method =="POST":
        name = request.form["username"]
    
    # .py -> html
    return render_template("sub.html", n = name)


if __name__ == "__main":
    app.run(debug=True)