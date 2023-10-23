import json
from flask import Flask, render_template

with open("data.json", "r") as f:
    data = json.load(f)
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    with open("data.json", "r") as f:
        data = json.load(f)

    return render_template("home.html", data=data)


@app.route('/post/<id>')
def show_post(id):
    for item in data:
        if item['id'] == id:
            return render_template("post.html", item=item)


app.run(host='0.0.0.0', port=80)
