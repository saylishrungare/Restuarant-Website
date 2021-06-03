from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sayli123@localhost/restaurant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class reservation(db.Model):
    __tablename__ = 'reservevation'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True) 
    mail = db.Column(db.String(200) ) 
    phone = db.Column(db.String(200) )
    people = db.Column(db.String(200))
    date = db.Column(db.Date )
    msg = db.Column(db.String(200))

    def __init__(self, customer, mail, phone, people, date, msg):
        self.customer = customer
        self.mail = mail
        self.phone = phone
        self.people = people
        self.date = date
        self.msg = msg

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/reservation')
def reserve():
    return render_template("reservation.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/submit', methods=['POST'])   
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        mail = request.form['mail']
        phone = request.form['phone']
        people = request.form['people']
        date = request.form['date']
        msg = request.form['msg']
        data = reservation(customer,mail,phone,people,date,msg)
        db.session.add(data)
        db.session.commit()
        return render_template("s.html")

if __name__ == "__main__":
    app.debug = True
    app.run()