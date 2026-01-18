import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "ml-reco-secret")

    # Render → Neon provides DATABASE_URL automatically
    # Local → fallback SQLite
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///ml_recommendations.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Extra safety (works together with extensions.py)
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 300,  # recycle connections every 5 minutes
    }
