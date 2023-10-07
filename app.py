import os 
from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI']  = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI']  = 'postgresql://default:TiXOFWB9j4Kf@ep-late-cell-64247649.us-east-1.postgres.vercel-storage.com/verceldb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = False

db = SQLAlchemy(app)

class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teacher = db.Column(db.String(100), nullable=False)
    #lastname = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(80), unique=True, nullable=False)
    room = db.Column(db.Integer)
    # i dont think we need this + it uses sq lite
    # created_at = db.Column(db.DateTime(timezone=True),
    #                       server_default=func.now())
    status = db.Column(db.Text)

    def __repr__(self):
        return f'<tutorial {self.teacher}>'


#@app.route("/")
def hello_world():
    return 'Hello World!'

# ...

@app.route('/')
def index():
    classes = Classes.query.all()
    return render_template('index.html', classes=classes)

@app.route('/aboutme/')
def aboutme():
    classes = Classes.query.all()
    return render_template('aboutme.html', classes=classes)

@app.route('/contactus/')
def contactus():
    classes = Classes.query.all()
    return render_template('contactus.html', classes=classes)

@app.route('/index/')
def contactus():
    classes = Classes.query.all()
    return render_template('index.html', classes=classes)

# ...


@app.route('/<id>/edit/', methods=('GET', 'POST'))
def edit(id):
    teacher = Classes.query.get_or_404(id)

    if request.method == 'POST':
        #name = request.form['teacher']
        status = request.form['status']
        #room = request.form['room']

        #teacher.name = name
        teacher.status = status
        #teacher.room = room

        db.session.add(teacher)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', classes=teacher)


if __name__ == "__main__":
    app.run()

# python3 -m flask run