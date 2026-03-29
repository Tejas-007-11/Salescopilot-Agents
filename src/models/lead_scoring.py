def score_lead(industry, company_size):
    score = 0

    if industry in ["SaaS", "FinTech"]:
        score += 40
    else:
        score += 20

    if company_size > 200:
        score += 40
    else:
        score += 20

    return score