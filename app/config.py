import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "ml-reco-secret")

    # Local → SQLite
    # Render → Neon (DATABASE_URL auto injected)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///ml_recommendations.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
