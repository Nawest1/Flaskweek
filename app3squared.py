from flask import Flask

app = Flask(__name__)

@app.route('/squared/<number>')
def squared(number):
    x=(int(number))**2
    return str(x)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)