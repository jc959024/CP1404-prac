from flask import Flask, render_template
from temperatures import celsius_to_fahrenheit


app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return render_template("greet.html", name=name)


@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        celsius_float = float(celsius)
        fahrenheit = celsius_to_fahrenheit(celsius_float)
        return f"{celsius_float}°C is {fahrenheit:.2f}°F"
    except ValueError:
        return "Invalid input. Please enter a numeric value."


if __name__ == '__main__':
    app.run(debug=True)

