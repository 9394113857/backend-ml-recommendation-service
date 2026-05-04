# =====================================================
# FINAL RECOMMENDATION MODEL (MIGRATION SAFE ✅)  
# =====================================================

from app.extensions import db
from datetime import datetime


class Recommendation(db.Model):
    __tablename__ = "recommendations"

    # 🔥 COMPOSITE PRIMARY KEY
    user_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    product_id = db.Column(db.BigInteger, primary_key=True, nullable=False)

    # ML fields
    score = db.Column(db.Float, nullable=False)
    rank = db.Column(db.Integer, nullable=False)

    # timestamp
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=db.func.now()
    )

    # indexes
    __table_args__ = (
        db.Index("idx_user_reco", "user_id"),
        db.Index("idx_user_rank", "user_id", "rank"),
    )

    def to_dict(self):
        return {
            "user_id": int(self.user_id),
            "product_id": int(self.product_id),
            "score": float(self.score),
            "rank": int(self.rank),
            "created_at": self.created_at.isoformat() if self.created_at else None
        }