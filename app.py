from flask import Flask, app, jsonify, request
from database import db


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://admin:admin123@127.0.0.1:3306/daily_diet"

    db.init_app(app)
    db.create_all()
    app.run()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)