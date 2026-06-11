from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from models.faq_engine import get_answer

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    question = data["question"]

    answer = get_answer(question)

    if answer is None:
        answer = "Sorry, I don't know that yet."

    return jsonify({
        "answer": answer
    })

if _name_ == "_main_":
    app.run(debug=True)



