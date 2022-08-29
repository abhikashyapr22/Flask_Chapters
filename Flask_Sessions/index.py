from flask import Flask, request, redirect, url_for, escape, session, render_template

app = Flask(__name__)

app.secret_key = 'secret_key'


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'logged in as ' + username + "<br><b><a href='/logout'>click here to log out</a></b>"

    return "You are not logged in <br> <a href='/login'><b>click here to login</b></a>"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    print("You are logged out")
    return "You are logged out <br><a href='/login'><b>Click here to login again </b></a>"


if __name__ == "__main__":
    app.run(debug=True)