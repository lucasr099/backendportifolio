# backend-ai/routes/ai_routes.py
from flask import Blueprint, request, jsonify
from services.ai_service import gerar_resposta

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/gerar-resposta", methods=["POST"])
def responder():
    data = request.get_json()

    if "mensagem" not in data:
        return jsonify({"erro": "mensagem não encontrada"}), 400

    resposta = gerar_resposta(data["mensagem"])
    return jsonify({"resposta": resposta})
