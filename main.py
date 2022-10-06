from flask import Flask, render_template
import requests

app = Flask(__name__)
API_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"

access = requests.get(url=API_ENDPOINT).json()

@app.route('/')
def home():
    return render_template('index.html', contents=access)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/index.html')
def index():
    return render_template('index.html', contents=access)

@app.route('/<num>')
def post(num):
    return render_template('post.html', news=access[int(num)-1])


if __name__ == "__main__":
    app.run(debug=True)