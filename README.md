# 🛍️ Smart Retail Analytics: End-to-End Business Intelligence & ML Platform

A full-scale data analytics and machine learning solution built for a modern e-commerce environment. This project extracts deep business value from raw behavioral data — predicting churn, segmenting customers, forecasting demand, analyzing sentiment, and recommending products — all integrated into a real-world, business-facing dashboard.

---

## 🚀 Project Summary

Smart Retail Analytics is designed to replicate the analytical capabilities of a data science team embedded in a retail organization. From data wrangling to stakeholder-ready dashboards, the project delivers actionable insights using Python, Power BI, and advanced ML algorithms.

---

## 🔍 Key Modules & Deliverables

### 1. 🧠 Churn Prediction
- **Objective**: Predict if a customer will abandon cart behavior.
- **Methods**: Logistic Regression, Random Forest
- **Business Value**: Enables proactive retention strategies.
- **Outputs**: `cart_churn_dataset.csv`, feature importance plots, churn driver insights.

---

### 2. 👥 Customer Segmentation (RFM + KMeans)
- **Objective**: Group users based on Recency, Frequency, and Monetary value.
- **Methods**: RFM Analysis + KMeans Clustering
- **Business Value**: Drives targeted marketing campaigns and customer lifecycle strategy.
- **Outputs**: `rfm_segments.csv`, segment-wise behavior summary.

---

### 3. 📈 Demand Forecasting
- **Objective**: Predict daily sales for top-selling products over the next 30 days.
- **Methods**: Facebook Prophet
- **Business Value**: Supports inventory planning and sales strategy.
- **Outputs**: 10 CSV forecasts in `/forecast_outputs/`, line charts per product.

---

### 4. 💬 Sentiment Analysis (NLP)
- **Objective**: Classify product reviews into positive, negative, or neutral.
- **Methods**: TF-IDF + Logistic Regression
- **Business Value**: Captures customer satisfaction and pain points.
- **Outputs**: `sentiment_summary.csv`, word clouds, class balance charts.

---

### 5. 🛒 Product Recommendation Engine
- **Objective**: Suggest top 5 products for each user.
- **Methods**: Collaborative Filtering (SVD via Surprise)
- **Business Value**: Enhances user engagement and cross-sell performance.
- **Outputs**: `recommendations.csv`, user-product suggestion table.

---

## 🛠 Tech Stack

| Category          | Tools/Packages                                     |
|-------------------|----------------------------------------------------|
| Data Processing   | Python, Pandas, NumPy                              |
| ML & Forecasting  | Scikit-learn, Prophet, Surprise, KMeans            |
| NLP               | NLTK, TF-IDF Vectorizer                            |
| Visualization     | Power BI, Seaborn, Matplotlib, WordCloud           |
| Dashboarding      | Power BI (desktop), Streamlit deployment |
| Project Structure | GitHub, Jupyter Notebooks                          |

---

## 📁 Project Structure
smart-retail-analytics/
├── data/
│ ├── raw/
│ └── processed/
├── notebooks/
│ ├── 01_EDA.ipynb
│ ├── 02_Churn_Model.ipynb
│ ├── 03_Segmentation.ipynb
│ ├── 04_Demand_Forecast.ipynb
│ ├── 05_Sentiment_NLP.ipynb
│ └── 06_Recommender.ipynb
├── visuals/
├── dashboard/
│ ├── SmartRetailDashboard.pbix
│ └── app.py
├── requirements.txt
├── LICENSE
└── README.md


---

## 🧠 Business Use Cases

- Retarget high-risk users with personalized offers
- Run lifecycle-based campaigns by segment
- Plan product stocking with forward-looking forecasts
- Track voice of the customer with real-time sentiment
- Drive cross-sell revenue using personalized recommendations

---

## ✅ How to Run

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/smart-retail-analytics.git
    cd smart-retail-analytics

2.  python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate (Windows)
    pip install -r requirements.txt

3.  jupyter notebook
