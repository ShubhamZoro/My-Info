from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import datetime
import os
x = datetime.datetime.now()
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.yourmailserver.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('email')
app.config['MAIL_PASSWORD'] = os.getenv('password')

mail = Mail(app)


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html",year=x.year)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    msg = Message('Contact Form Submission', sender=email, recipients=[os.getenv('email')])
    msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'

    mail.send(msg)

    return render_template('success.html')


if __name__=='__main__':
    app.run(debug=True)
