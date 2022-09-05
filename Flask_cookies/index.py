from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def set_cookie():
    if request.method == "POST":
        user = request.form['nm']
        resp = make_response(render_template('readcookie.html', user=user))
        resp.set_cookie('userID', user)
        return resp


@app.route('/getcookie')
def get_cookie():
    name = request.cookies.get('userID')
    return '<h1> Welcome ' + name + '</h1>'


if __name__ == "__main__":
    app.run(debug=True)
