import os 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False

db = SQLAlchemy(app)

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    room = db.Column(db.Integer)
    # i dont think we need this + it uses sq lite
    # created_at = db.Column(db.DateTime(timezone=True),
    #                       server_default=func.now())
    status = db.Column(db.Text)

    def __repr__(self):
        return f'<Teacher {self.firstname}>'


@app.route("/")
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run()

# python3 -m flask run