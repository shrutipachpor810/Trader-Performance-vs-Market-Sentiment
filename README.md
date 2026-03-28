# 📊 **Trader Behavior vs Market Sentiment Analysis**

---

## 📌 **Objective**

This project analyzes how **market sentiment (*Fear/Greed Index*)** influences **trader behavior and performance** using Hyperliquid trading data.

The goal is to uncover ***actionable insights*** that can inform **smarter trading strategies**.

---

## 📂 **Datasets Used**

### 🔹 *Bitcoin Market Sentiment Dataset*

* **Columns:** Date, Classification (*Extreme Fear → Extreme Greed*)

### 🔹 *Historical Trader Data (Hyperliquid)*

* Includes:

  * Account
  * Execution Price
  * Size
  * Side
  * Closed PnL
  * Timestamp

---
##*Outputs*
**This are from Streamlit dashboard** 
<img width="1910" height="962" alt="image" src="https://github.com/user-attachments/assets/6b3dc924-5eab-421d-a5ef-3ca25fb5a0cf" />

<img width="930" height="840" alt="image" src="https://github.com/user-attachments/assets/4b9b8102-f953-4829-b374-d33255220c38" />

<img width="920" height="876" alt="image" src="https://github.com/user-attachments/assets/914c3123-2c34-467a-97ef-60111e553685" />

<img width="915" height="846" alt="image" src="https://github.com/user-attachments/assets/b540e9af-36bc-48d9-85a3-63720fbf3786" />

<img width="897" height="348" alt="image" src="https://github.com/user-attachments/assets/cde1cb43-1a8c-43a6-a92a-67c11ddbf1fb" />

**This are from analysis**

<img width="711" height="653" alt="image" src="https://github.com/user-attachments/assets/4ee4c8fd-e365-4824-a3e2-4ceb640ebd52" />

<img width="817" height="573" alt="image" src="https://github.com/user-attachments/assets/81707c3b-1a0e-43a9-9e0d-ca6f9fb20ecf" />

<img width="756" height="567" alt="image" src="https://github.com/user-attachments/assets/4829bf05-3e0b-47cb-b158-9aae61e93f62" />

## ⚙️ **Methodology**

### **1. Data Preparation**

* Cleaned *missing values* and removed duplicates
* Converted timestamps to **daily format**
* Merged sentiment and trading datasets based on date

### **2. Feature Engineering**

* Daily **PnL per trader**
* **Win rate** (*% profitable trades*)
* Trade frequency
* Average **position size (Size USD)**
* **Leverage proxy**
* **Long/Short bias**

---

## 📊 **Analysis Performed**

### 🔹 **Performance vs Sentiment**

* Compared:

  * **PnL**
  * **Win rate**
  * **Drawdown (loss proxy)**
    across different sentiment categories

---

### 🔹 **Behavioral Analysis**

* Trade frequency changes
* Position size variation
* Leverage usage
* Long vs Short bias

---

### 🔹 **Trader Segmentation**

* **High vs Low leverage traders**
* **Frequent vs Infrequent traders**
* **Winners vs Losers**

---

## 🔥 **Key Insights**

* **Extreme Greed** yields the *highest profitability* (~205 avg PnL) but also **higher risk**
* **Position size** has a stronger impact on performance than leverage
* Traders increase exposure during **Fear and Greed**, leading to **higher volatility**
* **Sentiment intensity** (*not just direction*) significantly affects behavior and outcomes
* High leverage amplifies gains in bullish markets but increases losses in uncertain conditions

---

## 🎯 **Strategy Recommendations**

* Reduce **position size** during *Fear / Extreme Fear* markets
* Avoid combining **high leverage + large position sizes**
* Gradually scale positions during *Greed / Extreme Greed*
* Adapt strategies based on ***sentiment intensity***, not just direction

---

## 🤖 **Bonus Work**

### ✔ **Predictive Modeling**

* Built a **Random Forest model** to predict trade profitability
* Found: ***Position size > leverage*** in importance

---

### ✔ **Trader Clustering**

Identified behavioral archetypes:

* 🔺 *High-risk traders*
* 🟢 *Conservative traders*
* ⭐ *Consistent performers*

---

### ✔ **Streamlit Dashboard**

Interactive dashboard to explore:

* PnL trends
* Win rate
* Position size
* Long/Short bias

---

## 🖥️ **How to Run**

### **1. Clone the repository**

```bash
git clone https://github.com/shrutipachpor810/trader-sentiment-analysis.git
cd trader-sentiment-analysis
```

### **2. Create virtual environment**

```bash
python -m venv venv
```

### **3. Activate environment**

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### **4. Install dependencies**

```bash
pip install -r requirements.txt
```

### **5. Run Streamlit dashboard**

```bash
streamlit run app.py
```

---

## 📁 **Project Structure**

```
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
```

---

## 📌 **Conclusion**

Trader performance is strongly influenced by **market sentiment and behavioral factors**.

Effective risk management — especially controlling ***position size*** — is more critical than leverage alone.

Adapting strategies based on ***sentiment intensity*** can significantly improve trading outcomes.

---

## 👩‍💻 **Author**

**Shruti Pachpor**
*Data Science / Analytics Enthusiast*
