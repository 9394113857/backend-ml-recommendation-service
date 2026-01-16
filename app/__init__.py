from flask import Flask, jsonify
from app.config import Config
from app.extensions import db, migrate, cors
from app.routes import recommendations_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # ---------------------------------------------
    # CORS (Angular / Netlify / Local)
    # ---------------------------------------------
    cors.init_app(app)

    # ---------------------------------------------
    # Extensions
    # ---------------------------------------------
    db.init_app(app)
    migrate.init_app(app, db)

    # ---------------------------------------------
    # Routes
    # ---------------------------------------------
    app.register_blueprint(recommendations_bp, url_prefix="/api")

    # ---------------------------------------------
    # Root Health Check
    # GET /
    # ---------------------------------------------
    @app.get("/")
    def health():
        return jsonify({"status": "ML-Recommendation-Service UP"}), 200

    # ---------------------------------------------
    # API Health Check (optional, consistent style)
    # GET /api/health
    # ---------------------------------------------
    @app.get("/api/health")
    def api_health():
        return jsonify({"status": "ml-recommendation-api UP"}), 200

    return app
