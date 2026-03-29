from flask import Flask, render_template, request, jsonify
import sys
import os

# Fix imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.prospecting_agent import run_prospecting
from agents.deal_agent import analyze_deal
from agents.retention_agent import analyze_customer

app = Flask(__name__)

# ------------------------
# Home Page
# ------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ------------------------
# Prospecting API
# ------------------------
@app.route("/prospect", methods=["POST"])
def prospect():
    data = request.json
    score, email = run_prospecting(
        data["company"], data["industry"], data["size"]
    )
    return jsonify({"score": score, "email": email})

# ------------------------
# Deal Intelligence API
# ------------------------
@app.route("/deal", methods=["POST"])
def deal():
    data = request.json
    risk, response = analyze_deal(
        data["days"], data["response"], data["competitor"]
    )
    return jsonify({"risk": risk, "response": response})

# ------------------------
# Churn API
# ------------------------
@app.route("/churn", methods=["POST"])
def churn():
    data = request.json

    pred, prob, explanation = analyze_customer(data)

    return jsonify({
        "probability": prob,
        "explanation": explanation
    })

# ------------------------
# Run
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)