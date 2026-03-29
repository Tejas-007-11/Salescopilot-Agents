from llm.llm_utils import generate_text

def analyze_deal(last_contact_days, response_rate, competitor_flag):
    risk = "Low"

    if last_contact_days > 10 or response_rate < 0.3:
        risk = "Medium"

    if competitor_flag == 1 and response_rate < 0.3:
        risk = "High"

    prompt = f"""
You are a senior B2B sales strategist.

A deal has the following signals:
- Last contact: {last_contact_days} days ago
- Response rate: {response_rate}
- Competitor mentioned: {competitor_flag}

Give:
1. Risk explanation
2. Specific recovery strategy
3. A short client message (2-3 lines)
Keep it concise and actionable.
"""

    ai_response = generate_text(prompt)

    return risk, ai_response