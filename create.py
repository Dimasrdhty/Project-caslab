from flask import Flask
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgres://wmfjnbbwgxwzyn:4c1f1d3dc292ef7315fe3bdfce93f5b070eb3b444b34830d3f0408aaf27e55ec@ec2-54-237-135-248.compute-1.amazonaws.com:5432/d2b54gvvqi9a4d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
