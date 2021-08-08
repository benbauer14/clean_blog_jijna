from flask import Flask, url_for
from flask.templating import render_template
import requests
import random

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/about')
def about():
    return(render_template('about.html'))

@app.route('/contact')
def contact():
    return(render_template('contact.html'))

@app.route('/post')
def post():
    blogdata = requests.get("https://api.npoint.io/43644ec4f0013682fc0d")
    blog = blogdata.json()
    print(blog)
    return(render_template('post.html'))

if __name__ == "__main__":
    app.run(debug=True)