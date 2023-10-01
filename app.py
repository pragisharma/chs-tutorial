from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()

# python3 -m flask run