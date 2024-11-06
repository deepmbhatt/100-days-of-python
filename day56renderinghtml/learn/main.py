from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/aboutme")
def aboutme():
    return render_template("about_me.html")

@app.route("/website")
def website():
    return render_template("personal.html")

if __name__ == "__main__":
    app.run(debug=True)