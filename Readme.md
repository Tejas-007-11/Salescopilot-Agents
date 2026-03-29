# 🚀 SalesCopilot AI
### AI-Powered Sales & Revenue Intelligence System

SalesCopilot AI is a multi-agent AI system that helps sales teams improve conversions, reduce churn, and take smarter actions using AI. It combines Machine Learning for prediction and a Local LLM for reasoning and decision-making.

---

## 📌 Problem

- Sales teams miss early warning signals in deals
- Outreach is often generic and ineffective
- Churn is detected too late
- Data exists but is not actionable
- Decision-making is reactive instead of proactive

---

## 💡 Solution

SalesCopilot AI acts as an intelligent co-pilot that:
- Identifies high-quality prospects
- Detects deal risks in real time
- Predicts customer churn
- Recommends exact actions to improve outcomes
- Converts raw data into actionable insights

---

## 🧠 Key Features

### 📊 Prospecting Agent
- Scores leads based on company inputs
- Generates personalized outreach emails
- Improves targeting and engagement

### ⚠️ Deal Intelligence Agent
- Detects deal risk using engagement signals
- Identifies inactivity and response drops
- Suggests recovery strategies and messaging

### 📉 Retention Agent
- Predicts churn using ML model
- Explains risk based on input data
- Suggests actions aligned with risk level

---

## ⚙️ Architecture Overview

- Frontend: Flask-based web interface
- Backend: REST API handling requests
- Agents:
  - Prospecting Agent
  - Deal Intelligence Agent
  - Retention Agent
- ML Layer:
  - Random Forest model for churn prediction
- LLM Layer:
  - Local LLM (Phi-3 via Ollama)
- Data:
  - Synthetic dataset (customers.csv)
  - Trained model (churn_model.pkl)

---

## 🔄 Workflow

1. User enters input in UI
2. Request goes to Flask backend
3. Agent processes the request
4. ML model predicts churn (if needed)
5. LLM generates explanation and actions
6. Output is displayed to the user

---

## 🛠️ Tech Stack

- Python
- Flask
- HTML, CSS, JavaScript
- Scikit-learn
- Pandas
- Joblib
- Ollama (Phi-3 LLM)

---

## 📁 Project Structure

salescopilot-ai/
│
├── src/
│   ├── app/
│   │   ├── app.py
│   │   └── templates/
│   │       └── index.html
│   │
│   ├── agents/
│   │   ├── prospecting_agent.py
│   │   ├── deal_agent.py
│   │   └── retention_agent.py
│   │
│   ├── models/
│   │   ├── churn_model.py
│   │   └── churn_model.pkl
│   │
│   ├── llm/
│   │   └── llm_utils.py
│   │
│   └── data/
│       └── customers.csv
│
├── notebooks/
│   └── model.ipynb
│
└── README.md

---

## ▶️ Setup

### 1. Install dependencies
pip install flask pandas scikit-learn joblib requests

### 2. Setup LLM
ollama pull phi3
ollama run phi3

### 3. Run app
cd src/app
python app.py

Open:
http://127.0.0.1:5000

---

## 📊 Use Cases

- Generate personalized sales emails
- Detect risky deals early
- Predict customer churn
- Suggest actions for retention
- Improve sales decision-making

---

## 🚀 Innovation

- Combines ML prediction + LLM reasoning
- Multi-agent architecture
- Risk-aware decision system
- Runs locally with no external API dependency
- Focuses on actions, not just insights

---

## 🔮 Future Scope

- CRM integration
- Real-time enterprise data
- Fully autonomous workflows
- Advanced analytics dashboard
- Voice-enabled AI assistant

---

## 🎤 Final Note

SalesCopilot AI transforms sales from reactive tracking to proactive decision-making by combining predictive intelligence with actionable AI.