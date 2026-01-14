from flask import Flask
from app.config import Config
from app.extensions import db, migrate, cors
from app.routes import recommendations_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(recommendations_bp, url_prefix="/api")

    return app
