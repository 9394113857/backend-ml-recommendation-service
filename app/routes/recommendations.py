from flask import Blueprint, jsonify
from app.models import Recommendation

recommendations_bp = Blueprint("recommendations", __name__)

@recommendations_bp.get("/recommendations/<int:user_id>")
def get_recommendations(user_id):
    rows = (
        Recommendation.query
        .filter_by(user_id=user_id)
        .order_by(Recommendation.rank)
        .all()
    )

    return jsonify([
        {
            "product_id": r.product_id,
            "score": r.score,
            "rank": r.rank,
            "model_version": r.model_version
        }
        for r in rows
    ])
