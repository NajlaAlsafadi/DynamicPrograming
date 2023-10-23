import json
from flask import Flask, render_template

with open("data.json", "r") as f:
    data = json.load(f)
app = Flask(__name__)


@app.route('/post/<id>')
def show_post(id):
    for item in data:
        if item['id'] == id:
            # Render the content page template with the item data
            return render_template("post.html", item=item)


app.run(host='0.0.0.0', port=81)
