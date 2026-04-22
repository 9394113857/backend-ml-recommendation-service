# =========================
# Cell 2: Recommendations Route (FINAL)
# =========================

from flask import Blueprint, jsonify
from app.models.recommendation import Recommendation

recommendations_bp = Blueprint("recommendations", __name__)


# =========================================================
# GET USER RECOMMENDATIONS
# =========================================================
@recommendations_bp.get("/<int:user_id>")
def get_recommendations(user_id):

    rows = (
        Recommendation.query
        .filter_by(user_id=user_id)
        .order_by(Recommendation.rank.asc())
        .limit(10)
        .all()
    )

    if not rows:
        return jsonify({
            "message": "No recommendations found",
            "user_id": user_id
        }), 404

    return jsonify([
        {
            "user_id": r.user_id,
            "product_id": r.product_id,
            "score": r.score,
            "rank": r.rank
        }
        for r in rows
    ])
