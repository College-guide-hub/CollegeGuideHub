from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "College Guide Hub Running"

if _name_ == "_main_":
    app.run()
