# =========================
# Cell 1: Recommendation Model (FINAL - PRODUCTION SAFE)
# =========================

from app.extensions import db
from datetime import datetime


class Recommendation(db.Model):
    __tablename__ = "recommendations"

    # =========================
    # PRIMARY KEYS (Composite)
    # =========================
    user_id = db.Column(db.BigInteger, primary_key=True)
    product_id = db.Column(db.BigInteger, primary_key=True)

    # =========================
    # ML SCORE
    # =========================
    score = db.Column(db.Float, nullable=False)

    # =========================
    # RANK (Top-N)
    # =========================
    rank = db.Column(db.Integer, nullable=False)

    # =========================
    # TIMESTAMP
    # =========================
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    # =========================
    # INDEXES (PERFORMANCE)
    # =========================
    __table_args__ = (
        db.Index("idx_user_reco", "user_id"),
        db.Index("idx_user_rank", "user_id", "rank"),  # 🔥 fast top-N queries
    )

    # =========================
    # OPTIONAL: SERIALIZATION
    # =========================
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "product_id": self.product_id,
            "score": self.score,
            "rank": self.rank,
            "created_at": self.created_at.isoformat()
        }

    # =========================
    # DEBUG PRINT
    # =========================
    def __repr__(self):
        return (
            f"<Recommendation user={self.user_id} "
            f"product={self.product_id} rank={self.rank} score={self.score}>"
        )
