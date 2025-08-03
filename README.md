# 🚖 Uber Requests Supply-Demand Gap Analysis

This repository presents an exploratory data analysis (EDA) project on Uber ride requests with the aim of identifying and analyzing the **supply-demand gap** in ride requests.

---

## 📂 Project Structure

- `UberSupplyDemand.ipynb` – Complete Jupyter notebook with data cleaning, feature engineering, visualizations, and insights.
- `Uber Request Data Cleaned.csv` – Cleaned dataset used for analysis.
- `Dashboard-Uber.xlsx` – Optional dashboard representation (if included).

---

## 🧠 Problem Statement

Uber faces an operational challenge due to a mismatch in customer ride requests and driver availability. This project analyzes ride request data to understand:

- When and where ride demand exceeds supply.
- Which time slots face the most cancellations or unavailability.
- Patterns by pickup point, time of day, and request status.

---

## 🔍 Data Overview

- Date Range: July 2016
- Columns: Request timestamp, Drop timestamp, Status, Pickup Point
- Status Types:
  - **Trip Completed**
  - **Cancelled**
  - **No Cars Available**

---

## 📊 Key Visualizations

- 📌 Requests vs Status (Bar Plot)
- 📌 Hourly demand trend (Histogram & Countplot)
- 📌 Time slot impact on status
- 📌 Pickup point analysis
- 📌 Violin and Box plots for request distribution
- 📌 Heatmap of correlation
- 📌 Stacked area chart for hour-wise status trends

---

## 💡 Business Insights

- **Morning hours (5–10 AM)** from the **city** see a surge in cancellations.
- **Evening hours (5–9 PM)** from the **airport** suffer from "No Cars Available".
- The gap is largely due to driver unavailability during peak hours.
- More vehicles should be allocated at specific **pickup points** and **time slots**.

---

## ✅ Recommendations

- **Dynamic driver allocation** based on time-slot demand.
- **Incentives for drivers** during peak demand hours.
- **Demand forecasting** using this historical data for proactive supply adjustment.

---

## 🛠️ Tech Stack

- Python (Pandas, Matplotlib, Seaborn)
- Jupyter Notebook
- Git / GitHub for version control
- Excel (optional dashboard)

---

## 📌 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/iam-krishna5/Uber-Requests-EDA.git
