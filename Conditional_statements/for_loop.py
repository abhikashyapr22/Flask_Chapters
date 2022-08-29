from flask import Flask, render_template

app = Flask(__name__)


@app.route('/result')
def result():
    d = {
        'Phy': 50,
        "Che": 60,
        "maths": 70
    }

    return render_template('forloop.html', result=d)


if __name__ == '__main__':
    app.run(debug=True)