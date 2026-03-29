# 🚀 SalesCopilot AI  
### AI-Powered Sales & Revenue Intelligence System

SalesCopilot AI is a multi-agent AI system designed to transform sales workflows by combining machine learning predictions with LLM-driven decision-making. It enables teams to proactively manage prospects, detect deal risks, and reduce customer churn with actionable insights.

---

## 🧠 Problem Statement

Sales teams often operate reactively due to:
- Missed follow-ups and engagement signals  
- Lack of real-time deal risk detection  
- Poor personalization in outreach  
- Late identification of customer churn  
- Data-rich but insight-poor systems  

---

## 💡 Solution

SalesCopilot AI introduces an **agentic AI architecture** that:
- Automates prospecting and outreach  
- Monitors deal health in real-time  
- Predicts churn with ML models  
- Generates actionable strategies using LLMs  
- Adapts recommendations based on risk levels  

---

## ⚙️ Key Features

### 📊 Prospecting Agent
- Scores leads based on industry and company size  
- Generates personalized cold outreach emails using LLM  

### ⚠️ Deal Intelligence Agent
- Detects deal risk using engagement signals  
- Generates recovery strategies and client messaging  

### 📉 Retention Agent
- Predicts churn probability using ML (Random Forest)  
- Provides AI-driven explanations and retention actions  

---

## 🏗️ Architecture Overview

- **Frontend:** Flask + HTML dashboard  
- **Backend:** REST API with modular agent-based design  
- **ML Layer:** Random Forest model for churn prediction  
- **LLM Layer:** Local LLM (Phi-3 via Ollama) for reasoning and text generation  
- **Data Layer:** Synthetic dataset for training and testing  

---

## 🔄 Workflow

1. User inputs data through the web interface  
2. Flask backend routes requests to appropriate agents  
3. Agents process inputs using ML models and LLMs  
4. Outputs include predictions, insights, and recommended actions  
5. Results are displayed in real-time  

---

## 🧪 Tech Stack

- Python  
- Flask  
- Scikit-learn  
- Pandas  
- Ollama (Local LLM - Phi-3 / Mistral)  
- HTML, CSS, JavaScript  

---

## 📁 Project Structure

salescopilot-ai/
├── src/
│   ├── app/
│   │   ├── app.py                  # Flask backend (API + routing)
│   │   └── templates/
│   │       └── index.html          # Frontend UI (single file)
│   │
│   ├── agents/
│   │   ├── prospecting_agent.py    # Lead scoring + outreach generation
│   │   ├── deal_agent.py           # Deal risk detection + recovery strategy
│   │   └── retention_agent.py      # Churn prediction + retention actions
│   │
│   ├── models/
│   │   ├── churn_model.py          # ML model loader + prediction logic
│   │   └── churn_model.pkl         # Trained Random Forest model
│   │
│   ├── llm/
│   │   └── llm_utils.py            # Ollama (Phi-3) integration
│   │
│   ├── data/
│   │   └── customers.csv           # Synthetic dataset
│   │
│   └── notebooks/
│       └── model.ipynb             # Data generation + training pipeline
│
├── requirements.txt                # Project dependencies
├── README.md                       # Project documentation
└── .gitignore                      # Ignore unnecessary files

---

## 🚀 Getting Started

### 1️⃣ Clone Repository
```bash
git clone <your-repo-url>
cd salescopilot-ai

pip install -r requirements.txt

ollama run phi3:mini

cd src/app
python app.py

http://127.0.0.1:5000
```