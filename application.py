from flask import Flask, render_template

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
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # Check username exist
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "Someone else has taken"

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Success!"


    return render_template("index.html", form=reg_form)



if __name__ == "__main__":

    app.run(debug=True)
