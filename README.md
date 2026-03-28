📊 Trader Behavior vs Market Sentiment Analysis
📌 Objective

This project analyzes how market sentiment (Fear/Greed Index) influences trader behavior and performance using Hyperliquid trading data.
The goal is to uncover actionable insights that can inform smarter trading strategies.

📂 Datasets Used
Bitcoin Market Sentiment Dataset
Columns: Date, Classification (Extreme Fear → Extreme Greed)
Historical Trader Data (Hyperliquid)
Includes: Account, Execution Price, Size, Side, Closed PnL, Timestamp, etc.

⚙️ Methodology
1. Data Preparation
Cleaned missing values and removed duplicates
Converted timestamps to daily format
Merged sentiment and trading datasets on date
2. Feature Engineering
Daily PnL per trader
Win rate (profitable trades %)
Trade frequency
Average position size (Size USD)
Leverage proxy
Long/Short bias

📊 Analysis Performed
🔹 Performance vs Sentiment
Compared PnL, win rate, and drawdown (loss proxy) across sentiment categories
🔹 Behavioral Analysis
Trade frequency changes
Position size variation
Leverage usage
Long vs Short bias
🔹 Trader Segmentation
High vs Low leverage traders
Frequent vs Infrequent traders
Winners vs Losers

🔥 Key Insights
Extreme Greed yields the highest profitability (~205 avg PnL) but also higher risk
Position size has a stronger impact on performance than leverage
Traders increase exposure during Fear and Greed, leading to higher volatility
Sentiment intensity (not just direction) significantly affects behavior and outcomes
High leverage amplifies gains in bullish markets but increases losses in uncertain conditions

🎯 Strategy Recommendations
Reduce position size during Fear / Extreme Fear markets
Avoid combining high leverage + large position sizes
Gradually scale positions during Greed / Extreme Greed
Adapt trading strategies based on sentiment intensity, not just direction

🤖 Bonus Work
✔ Predictive Modeling
Built a Random Forest model to predict trade profitability
Found position size > leverage in importance
✔ Trader Clustering
Identified behavioral archetypes:
High-risk traders
Conservative traders
Consistent performers
✔ Streamlit Dashboard
Interactive dashboard to explore:
PnL trends
Win rate
Position size
Long/Short bias

🖥️ How to Run
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/trader-sentiment-analysis.git
cd trader-sentiment-analysis
2. Create virtual environment
python -m venv venv
3. Activate environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
4. Install dependencies
pip install -r requirements.txt
5. Run Streamlit dashboard
streamlit run app.py

📁 Project Structure
trader-sentiment-analysis/
│
├── data/
│   ├── fear_greed_index.csv
│   └── historical_data.csv
│
├── notebook/
│   └── analysis.ipynb
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore

📌 Conclusion

Trader performance is strongly influenced by market sentiment and behavioral factors.
Effective risk management — especially controlling position size — is more critical than leverage alone.
Adapting strategies based on sentiment intensity can significantly improve trading outcomes.

👩‍💻 Author

Shruti Pachpor
(Data Science / Analytics Enthusiast)