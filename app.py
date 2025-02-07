from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/words', methods=['POST'])
def get_words():
    words = request.form.get("words")
    w_count = 0
    c_count = 0
    for word in words.split( ):
        w_count += 1
        for char in word:
            c_count += 1
    avg_w_length = w_count / len(words)

    return render_template("results.html", avg_w_length=avg_w_length, w_count=w_count, c_count=c_count)