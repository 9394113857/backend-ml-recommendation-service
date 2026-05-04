# =====================================================
# Recommendation Model (FINAL - PRODUCTION SAFE ✅)
# =====================================================

from app.extensions import db
from datetime import datetime


class Recommendation(db.Model):
    __tablename__ = "recommendations"

    # =========================
    # PRIMARY KEYS
    # =========================
    user_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    product_id = db.Column(db.BigInteger, primary_key=True, nullable=False)

    # =========================
    # ML SCORE
    # =========================
    score = db.Column(db.Float, nullable=False)

    # =========================
    # RANK
    # =========================
    rank = db.Column(db.Integer, nullable=False)

    # =========================
    # TIMESTAMP (SAFE)
    # =========================
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=db.func.now()
    )

    # =========================
    # INDEXES
    # =========================
    __table_args__ = (
        db.Index("idx_user_reco", "user_id"),
        db.Index("idx_user_rank", "user_id", "rank"),
    )

    # =========================
    # SERIALIZATION
    # =========================
    def to_dict(self):
        return {
            "user_id": int(self.user_id),
            "product_id": int(self.product_id),
            "score": float(self.score),
            "rank": int(self.rank),
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f"<Reco user={self.user_id} product={self.product_id} rank={self.rank}>"