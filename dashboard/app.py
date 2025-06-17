import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="🛍️ Smart Retail Intelligence", layout="wide")
st.title("Smart Retail Intelligence Dashboard")

# --- Load data ---
churn = pd.read_csv("data/processed/cart_churn_dataset.csv", nrows=10000)
rfm = pd.read_csv("data/processed/rfm_segments.csv")
sentiment = pd.read_csv("data/processed/sentiment_summary.csv")
recs = pd.read_csv("data/processed/recommendations.csv")

# --- Churn Section ---
st.header("Customer Churn")
churn_rate = churn['churned'].mean()
st.metric(label="Churn Rate", value=f"{churn_rate:.2%}")
st.bar_chart(churn['churned'].value_counts())

# --- Sentiment Section ---
st.header("Review Sentiment Summary")
fig, ax = plt.subplots()
sns.barplot(data=sentiment, x='sentiment', y='count', ax=ax)
st.pyplot(fig)

# --- Customer Segments ---
st.header("Customer Segments")
segment_summary = rfm.groupby('Segment_Label').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': 'mean',
    'user_id': 'count'
}).rename(columns={'user_id': 'Customer Count'})
st.dataframe(segment_summary.round(2))

# --- Recommendations ---
st.header("Product Recommendations")
user_id = st.selectbox("Select a user", recs['user_id'].unique())
user_recs = recs[recs['user_id'] == user_id]
st.write("Top Recommendations:")
st.dataframe(user_recs[['product_id', 'score']].sort_values(by='score', ascending=False))
