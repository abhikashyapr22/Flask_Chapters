from flask import Flask, render_template, request, flash, redirect, url_for, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)
app.secret_key = 'secret_key'


class students(db.Model):
    id = db.Column('student', db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(6))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


db.create_all()


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/show')
def show_all():
    return render_template('index.html', students=students.query.all())


@app.route('/new', methods=['POST', 'GET'])
def new():
    if request.method == 'POST':
        if not request.form['name'] \
                or not request.form['city'] \
                or not request.form['addr'] \
                or not request.form['pin']:
            flash("please enter all the details", "error")
        else:
            student = students(request.form['name'], request.form['city'], request.form['addr'], request.form['pin'])
            db.session.add(student)
            db.session.commit()

            flash('Record added successfully')
            return redirect(url_for('home'))

            # return """
            # Record added successfully
            # <h3><a href="{{url_for('show_all')}}">See here current data</a></h3>
            # """

    return render_template('new.html')


if __name__ == "__main__":
    app.run(debug=True)