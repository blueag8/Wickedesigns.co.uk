import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_mail import Mail, Message


app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['MAIL_SERVER']= os.environ.get("MAIL_SERVER")
app.config['MAIL_PORT'] = os.environ.get("MAIL_PORT")
app.config['MAIL_USERNAME'] = os.environ.get("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


#set app variables

PAGE_ACCESS_TOKEN = os.environ.get('PAGE_ACCESS_TOKEN')

#home page

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")


@app.route('/resume')
def resume():
    return render_template("resume.html")


@app.route('/contact', methods =['GET','POST'])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        sender = request.form["senderEmail"]
        number = request.form["number"]
        recipient = os.environ.get("MAIL_USERNAME")
        msg = Message(subject="Enquiry",
            sender=sender,
            recipients=[recipient],
            body= "customer:" + " " + name + "\n" + "phone number:" + " " + number + "\n\n"  + message)
        mail.send(msg)
        flash("Thank you for the Message! I will reply as soon as I can.", category="message")
  
   
    return render_template("contact.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=False)
