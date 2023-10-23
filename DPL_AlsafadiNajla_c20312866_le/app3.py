import json
from flask import Flask, render_template

with open('data.json', 'r') as f:
    data = json.load(f)

articles = data

app = Flask(__name__)



@app.route('/')
def index():
    html = "<h1>Home page ! </h1><br>"
    html = html + "<b>Latest News:</b> <br>'"

    links = []
    for article in articles:
        link = '<a href="/article/{}">{}</a>'.format(article['id'], '-' + article['source'] + '-' + article['title'])
        links.append(link)
    return html + '<br>'.join(links)


@app.route('/article/<int:id>')
def show_article(id):
    # Look up the article in the list of articles
    article = None
    for a in articles:
        if a['id'] == id:
            article = a
            html = '<h4>POST:' + (article['title']) + '</h4>'
            return '{}{}</>'.format(article['id'], html + article['source'] + '-' + article[
                'content']) + ' <br></br> ' + '<a href="/">Back</a><br><a ' \
                                              'href="/">Home</a><br> '

    if article is not None:
        # Render the article template with the article data
        return render_template('post.html', source=article['source'], title=article['title'],
                               content=article['content'])
    else:
        # Render the error template
        return render_template('error.html')


app.run(host='0.0.0.0', port=83)
