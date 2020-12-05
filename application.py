from flask import Flask, render_template, redirect, url_for

from wtfforms_fields import *

from models import *

# Configure app
app = Flask(__name__)
app.secret_key = 'replace later'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://wmfjnbbwgxwzyn:4c1f1d3dc292ef7315fe3bdfce93f5b070eb3b444b34830d3f0408aaf27e55ec@ec2-54-237-135-248.compute-1.amazonaws.com:5432/d2b54gvvqi9a4d'
db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()

    # Update if validation is Success
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))


    return render_template("index.html", form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = LoginForm()
    # Check if validation Success
    if login_form.validate_on_submit():
        return "Logged in"

    return render_template("login.html", form=login_form)

if __name__ == "__main__":

    app.run(debug=True)
