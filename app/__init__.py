# =========================
# Cell 3: App Factory
# =========================

from flask import Flask, jsonify
from app.config import Config
from app.extensions import db, migrate, cors
from app.routes.recommendations import recommendations_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cors.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(recommendations_bp, url_prefix="/api")

    @app.get("/")
    def health():
        return jsonify({"status": "ML-Recommendation-Service UP"}), 200

    @app.get("/api/health")
    def api_health():
        return jsonify({"status": "ml-recommendation-api UP"}), 200

    return app
