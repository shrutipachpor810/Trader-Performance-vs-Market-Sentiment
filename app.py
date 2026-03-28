import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("📊 Trader Behavior vs Market Sentiment")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("historical_data.csv")
    sentiment = pd.read_csv("fear_greed_index.csv")

    # Parse sentiment dates with day-first format (e.g., 13-02-2018) and coerce invalid values
    sentiment['date'] = pd.to_datetime(sentiment['date'], dayfirst=True, errors='coerce').dt.date
    if sentiment['date'].isna().any():
        st.warning("Some sentiment dates could not be parsed and will be dropped.")
        sentiment = sentiment.dropna(subset=['date'])

    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms', errors='coerce')
    df['date'] = df['Timestamp'].dt.date

    df = df.merge(sentiment[['date','classification']], on='date', how='left')

    df['win'] = df['Closed PnL'] > 0
    df['leverage_proxy'] = df['Size USD'] / (df['Execution Price'] * df['Size Tokens'])
    df['is_long'] = df['Side'].apply(lambda x: 1 if str(x).lower() == 'buy' else 0)

    return df

df = load_data()

# Sidebar filter
st.sidebar.header("Filters")
sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df['classification'].unique(),
    default=df['classification'].unique()
)

filtered_df = df[df['classification'].isin(sentiment_filter)]

# =========================
# 📊 KPIs
# =========================
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg PnL", round(filtered_df['Closed PnL'].mean(),2))
col2.metric("Win Rate", round(filtered_df['win'].mean(),2))
col3.metric("Avg Position Size", round(filtered_df['Size USD'].mean(),2))

# =========================
# 📊 PnL by Sentiment
# =========================
st.subheader("PnL Distribution by Sentiment")

fig1, ax1 = plt.subplots()
sns.boxplot(x='classification', y='Closed PnL', data=filtered_df, ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# =========================
# 📊 Win Rate
# =========================
st.subheader("Win Rate by Sentiment")

win_rate = filtered_df.groupby('classification')['win'].mean().reset_index()

fig2, ax2 = plt.subplots()
sns.barplot(x='classification', y='win', data=win_rate, ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

# =========================
# 📊 Position Size
# =========================
st.subheader("Position Size by Sentiment")

fig3, ax3 = plt.subplots()
sns.barplot(x='classification', y='Size USD', data=filtered_df, ax=ax3)
plt.xticks(rotation=45)
st.pyplot(fig3)

# =========================
# 📊 Long vs Short
# =========================
st.subheader("Long vs Short Bias")

long_short = filtered_df.groupby('classification')['is_long'].mean().reset_index()

fig4, ax4 = plt.subplots()
sns.barplot(x='classification', y='is_long', data=long_short, ax=ax4)
plt.xticks(rotation=45)
st.pyplot(fig4)

# =========================
# 📋 Raw Data
# =========================
st.subheader("Raw Data Preview")
st.dataframe(filtered_df.head())