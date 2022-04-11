
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kesler-isoko.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'top secret!'
app.secret_key = 'password'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(port=3000,debug=True)