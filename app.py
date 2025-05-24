
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

WATI_API_TOKEN = os.getenv("WATI_API_TOKEN")
WATI_API_URL = "https://app.wati.io/api/v1/sendSessionMessage"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    user_number = data.get("waId")
    user_message = data.get("text", "").lower()

    # Simple intent logic
    if "price" in user_message:
        reply = "Our treatments start at ₹4500. Would you like the brochure?"
    elif "book" in user_message or "appointment" in user_message:
        reply = "Sure! I can help you schedule with Dr. Vaidehi. When would you like to come in?"
    else:
        reply = "Hi! This is Remya from Krása ✨ Let me know how I can assist you today."

    payload = {
        "phone": user_number,
        "message": reply
    }

    headers = {
        "Authorization": f"Bearer {WATI_API_TOKEN}",
        "Content-Type": "application/json"
    }

    requests.post(WATI_API_URL, json=payload, headers=headers)

    return jsonify({"status": "message sent"}), 200
