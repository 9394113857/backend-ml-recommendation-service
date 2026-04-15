# =========================
# Cell 1: Recommendation Model
# =========================

from app.extensions import db
from datetime import datetime


class Recommendation(db.Model):
    __tablename__ = "recommendations"

    # Composite Primary Key (IMPORTANT)
    user_id = db.Column(db.BigInteger, primary_key=True)
    product_id = db.Column(db.BigInteger, primary_key=True)

    # Match ML output
    score = db.Column(db.Float, nullable=False)

    # Ranking position
    rank = db.Column(db.Integer, nullable=False)

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Recommendation user={self.user_id} product={self.product_id} rank={self.rank}>"
