from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """This is Sabina's Jenkins project!"""


if __name__ == "__main__":
    app.run(host='localhost', port=5000)