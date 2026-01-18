from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from sqlalchemy.pool import NullPool

# 🔥 IMPORTANT:
# - pool_pre_ping=True → checks if DB connection is alive
# - NullPool → avoids reusing dead Neon SSL connections
# This combination is REQUIRED for Neon + Render stability

db = SQLAlchemy(
    engine_options={
        "poolclass": NullPool,
        "pool_pre_ping": True,
    }
)

migrate = Migrate()
cors = CORS()
