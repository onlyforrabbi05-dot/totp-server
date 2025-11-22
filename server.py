from flask import Flask, request, jsonify
import pyotp

app = Flask(__name__)

@app.route("/totp", methods=["POST"])
def generate_totp():
    data = request.get_json()
    secret = data.get("secret")

    if not secret:
        return jsonify({"error": "no secret"}), 400

    try:
        totp = pyotp.TOTP(secret)
        return jsonify({"code": totp.now()})
    except:
        return jsonify({"error": "invalid secret"}), 400

@app.route("/", methods=["GET"])
def home():
    return "TOTP Server Running"
