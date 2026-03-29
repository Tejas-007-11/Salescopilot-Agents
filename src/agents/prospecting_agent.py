from models.lead_scoring import score_lead
from llm.llm_utils import generate_text

def run_prospecting(company, industry, size):
    score = score_lead(industry, size)

    prompt = f"""
    You are a B2B sales expert.

    Write a short, high-converting cold email for:
    Company: {company}
    Industry: {industry}

    Keep it:
    - Personalized
    - Professional
    - Under 120 words
    - Include a clear call-to-action
    """

    email = generate_text(prompt)

    return score, email