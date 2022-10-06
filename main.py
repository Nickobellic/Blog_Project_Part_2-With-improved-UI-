from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
API_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"
my_email = "avrahulkanna17@gmail.com"
passw = "avcqikybvlvjahyw"

smtp = smtplib.SMTP("smtp.gmail.com")
smtp.starttls()
smtp.login(user=my_email, password=passw)


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

@app.route('/contact.html', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        smtp.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Login Details \n\n Name: {request.form['name']}\n Email: {request.form['email']}\n Phone Number: {request.form['phone']}\nMessage: {request.form['message']}")
        smtp.close()
        return render_template('contact.html', mess="Successfully sent your message")



if __name__ == "__main__":
    app.run(debug=True)