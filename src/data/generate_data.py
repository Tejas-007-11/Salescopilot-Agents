import pandas as pd
import random
from faker import Faker

fake = Faker()

# ----------------------
# Leads Dataset
# ----------------------
def generate_leads(n=100):
    industries = ["SaaS", "FinTech", "Healthcare", "E-commerce", "EdTech"]

    data = []
    for _ in range(n):
        data.append({
            "company_name": fake.company(),
            "industry": random.choice(industries),
            "company_size": random.choice([10, 50, 100, 500, 1000]),
            "location": fake.city(),
            "website": fake.url()
        })

    return pd.DataFrame(data)

# ----------------------
# Deals Dataset
# ----------------------
def generate_deals(leads_df):
    data = []

    for i, row in leads_df.iterrows():
        data.append({
            "deal_id": i,
            "company_name": row["company_name"],
            "deal_stage": random.choice(["Lead", "Qualified", "Proposal", "Negotiation"]),
            "deal_value": random.randint(5000, 50000),
            "last_contact_days": random.randint(0, 30),
            "email_response_rate": round(random.uniform(0, 1), 2),
            "competitor_mentioned": random.choice([0, 1])
        })

    return pd.DataFrame(data)

# ----------------------
# Customers Dataset
# ----------------------
def generate_customers(n=100):
    data = []

    for i in range(n):
        login_freq = random.randint(0, 10)
        last_active = random.randint(0, 30)

        churn = 1 if (login_freq < 3 and last_active > 10) else 0

        data.append({
            "customer_id": i,
            "login_frequency": login_freq,
            "feature_usage": random.randint(1, 10),
            "support_tickets": random.randint(0, 5),
            "last_active_days": last_active,
            "subscription_plan": random.choice(["Basic", "Pro", "Enterprise"]),
            "churn": churn
        })

    return pd.DataFrame(data)


if __name__ == "__main__":
    leads = generate_leads()
    deals = generate_deals(leads)
    customers = generate_customers()

    leads.to_csv("data/raw/leads.csv", index=False)
    deals.to_csv("data/raw/deals.csv", index=False)
    customers.to_csv("data/raw/customers.csv", index=False)

    print("✅ Synthetic datasets generated!")