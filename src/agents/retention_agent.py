from models.churn_model import predict_churn
from llm.llm_utils import generate_text

def analyze_customer(data):
    prediction, prob = predict_churn(data)

    prompt = f"""
You are a customer success expert.

Customer data:
{data}

Churn probability: {prob}

Rules:
- If probability < 0.3 → LOW risk → give light suggestions only
- If 0.3 to 0.7 → MEDIUM risk → moderate intervention
- If > 0.7 → HIGH risk → strong retention actions

Important:
- Do not make assumptions beyond the given data
- Keep reasoning grounded in the input values
- Do not use asterisks or special formatting symbols

Output format:

Risk Level: <Low/Medium/High>

Why:
(1 to 2 short lines, based only on input data)

Action:
(1 to 2 simple, practical steps aligned with risk level)

Keep the response concise and professional.
"""

    explanation = generate_text(prompt)

    return prediction, prob, explanation