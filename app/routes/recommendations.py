# =====================================================
# Recommendations Route (FINAL - PRODUCTION READY 🚀)
# =====================================================

from flask import Blueprint, jsonify, current_app
from app.models.recommendation import Recommendation

recommendations_bp = Blueprint("recommendations", __name__)


@recommendations_bp.get("/<int:user_id>")
def get_recommendations(user_id):

    current_app.logger.info(f"Fetching recommendations for user {user_id}")

    rows = (
        Recommendation.query
        .filter_by(user_id=user_id)
        .order_by(Recommendation.rank.asc())
        .limit(10)
        .all()
    )

    if not rows:
        current_app.logger.info(f"No recommendations found for user {user_id}")
        return jsonify([]), 200

    return jsonify({
        "user_id": user_id,
        "count": len(rows),
        "recommendations": [r.to_dict() for r in rows]
    }), 200