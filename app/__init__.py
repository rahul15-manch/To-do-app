#app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Create Database Object globaly 
db = SQLAlchemy()

def create_app():
    app=Flask(__name__)

    app.config["SECRET_KEY"]="your_secret_key"
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.tasks import task_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    return app