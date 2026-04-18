# =========================
# Cell 1: Recommendation Model (FINAL)
# =========================

from app.extensions import db
from datetime import datetime


class Recommendation(db.Model):
    __tablename__ = "recommendations"

    # Composite Primary Key
    user_id = db.Column(db.BigInteger, primary_key=True)
    product_id = db.Column(db.BigInteger, primary_key=True)

    # ML score
    score = db.Column(db.Float, nullable=False)

    # Rank (Top-N position)
    rank = db.Column(db.Integer, nullable=False)

    # Timestamp
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    # Index for faster queries
    __table_args__ = (
        db.Index("idx_user_reco", "user_id"),
    )

    def __repr__(self):
        return f"<Recommendation user={self.user_id} product={self.product_id} rank={self.rank}>"