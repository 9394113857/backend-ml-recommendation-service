from app.extensions import db
from datetime import datetime


class Recommendation(db.Model):
    __tablename__ = "recommendations"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False, index=True)
    product_id = db.Column(db.Integer, nullable=False)

    # ML score (renamed from weight)
    score = db.Column(db.Float, nullable=False)

    # Rank per user
    rank = db.Column(db.Integer, nullable=False)

    model_version = db.Column(db.String(50), nullable=False)

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Recommendation user={self.user_id} product={self.product_id} rank={self.rank}>"
