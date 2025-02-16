from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manutd.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your_secret_key'  # เพิ่ม SECRET_KEY สำหรับ WTForms

    db.init_app(app)

    # ลงทะเบียน Blueprint
    from .routes import main
    app.register_blueprint(main)

    return app
