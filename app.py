from flask import Flask, render_template

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if _name_ == "_main_":
    app.run(debug=True)
