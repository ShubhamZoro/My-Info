from flask import Flask, render_template

import datetime
import os
x = datetime.datetime.now()



app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html",year=x.year)




if __name__=='__main__':
    app.run(debug=True)
