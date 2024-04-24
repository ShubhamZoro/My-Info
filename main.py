from flask import Flask, render_template,request
from flask_mail import Mail, Message
import datetime
import os
app = Flask(__name__)
x = datetime.datetime.now()
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
email=os.environ.get('email')[0:len(os.environ.get('email'))]
app.config['MAIL_USERNAME'] = email
password=os.environ.get('password')[0:len(os.environ.get('password'))]
app.config['MAIL_PASSWORD'] = password

mail = Mail(app)


@app.route("/")
def hello_world():
    return render_template("index.html",year=x.year)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        sender_email = request.form['Email']
        message_body = request.form['message']
        message_subject=request.form['subject']
        # Send email
        msg=Message("This is an contact mail",sender=email,recipients=[email])
        msg.subject=message_subject
        msg.body = message_body+" "+sender_email
        mail.send(msg)

        return render_template("success.html") # Redirect to a success page after sending email



if __name__=='__main__':
    app.run(debug=True)


