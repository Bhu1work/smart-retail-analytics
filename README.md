# 🛍Smart Retail Intelligence Dashboard


## Live Demo
**[Launch Dashboard](https://smartretailanalytics.streamlit.app/)**  
**[View on GitHub](https://github.com/Bhu1work/smart-retail-analytics)**

---

## Project Overview

This project is an end-to-end **retail analytics and optimization platform** designed to simulate a real-world business intelligence solution. From raw user behavior logs to an interactive dashboard, this system supports decision-making in **churn prevention**, **customer segmentation**, **product recommendations**, and **sentiment monitoring**.

---

## Key Features

- **Churn Prediction**  
  Modeled user behavior leading to cart abandonment using Logistic Regression & Random Forest.

- **Sentiment Analysis**  
  Analyzed review sentiment polarity using NLP and visualized trends across product categories.

- **RFM-Based Customer Segmentation**  
  Used Recency, Frequency, Monetary scores to cluster customers into actionable personas.

- **Product Recommendations**  
  Built a personalized recommender system using matrix factorization techniques.

- **Forecasting**  
  Predicted demand trends using time series models like Prophet and ARIMA.

- **Interactive Streamlit Dashboard**  
  Hosted live with multi-tab insights, charts, and dynamic filters.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| `Python` | Core analytics and ML |
| `Pandas, NumPy` | Data manipulation |
| `Scikit-learn` | Churn prediction, ML models |
| `Seaborn, Matplotlib` | Static visualizations |
| `Streamlit` | Interactive dashboard |
| `Git LFS` | Handling large processed datasets |
| `Prophet, Surprise` | Time series & recommendation models |

---

## Project Structure
smart-retail-analytics/

├── data/

│ ├── raw/ # Ignored in .gitignore

│ └── processed/ # LFS tracked CSVs

├── notebooks/ # EDA & ML notebooks

├── scripts/ # Reusable Python scripts

├── dashboard/

│ └── app.py # Streamlit dashboard app

├── visuals/ # Screenshots & exports

├── requirements.txt

└── README.md


---

## Screenshots

| Churn Metrics | Customer Segments |
|---------------|--------------------|
| ![churn](visuals/churn_sample.png) | ![segments](visuals/segments_sample.png) |

---

## Author

**Bhuvan Sai Thatthari**  
📍 Data Analyst | M.S. in Data Analytics Engineering  
🔗 [LinkedIn](https://www.linkedin.com/in/your-profile) • [GitHub](https://github.com/Bhu1work)

---

## Future Enhancements

- Add deep learning model for sentiment classification  
- Improve recommender accuracy with hybrid models  
- CI/CD + Docker support for production readiness  

---

## Contributions

This is a solo-built portfolio project. For feedback or collaboration inquiries, feel free to open an issue or connect via LinkedIn.


