# 🌍 Forecasting Transport CO₂ Emissions with Machine Learning (SDG 13)

This project uses machine learning to **predict CO₂ emissions from transport** using key development indicators. It supports **UN Sustainable Development Goal 13 – Climate Action** by enabling smarter emission forecasting.

---

## 🔍 Problem Statement

As urbanization and economic growth increase, so do CO₂ emissions — especially in the transport sector. This project asks:

> Can we accurately forecast transport emissions using national development data?

---

## 🧠 ML Approach

We trained two models:
- ✅ **Random Forest Regressor** (final model)
- ❌ Linear Regression (baseline)

**Features used:**
- GDP per capita
- Population
- Urban Population %
- Energy Use per Capita

---

### 📈 Final Results 

# **Model:** Linear Regression  
**Evaluation:**

| Metric | Value |
|--------|-------|
| **MAE** | 207.16 | 
| **RMSE** | 415.76 |
| **R² Score** | 0.62 |

## interpretation of MAE: On average, our predictions are off by ~207 megatons of CO₂ — which is acceptable at a global scale.
## Interpretatiom of RMSE: Shows larger errors more strongly. A bit high, but expected due to variation across countries.
## Interpretation of R score: our model explains 62% of the variance in CO₂ transport emissions. That’s a good baseline!

# other explainations for random forest test can be found on the comments section of the jupyter file
## (Random Forest test one)

| Metric | Value |
|--------|-------|
| **MAE** | 8.39 |
| **RMSE** | 45.98 |
| **R² Score** | 1.00 |

Random Forest significantly outperformed Linear Regression (which had R² = 0.62).
 
## Results (Random Forest test two with reduced estimator from 100 to 50 and max depth of 10)
| Metric | Value |
|--------|-------|
| **MAE** | 9.80 |
| **RMSE** | 50.22 |
| **R² Score** | 0.99 |

---

## 📊 Datasets Used

All data was collected from [World Bank Open Data](https://data.worldbank.org/):

| Indicator | Code | Description |
|----------|------|-------------|
| CO₂ Emissions (Transport) | `EN.GHG.CO2.TR.MT.CE.AR5` | Annual emissions from transport (MtCO₂e) |
| GDP per Capita | `NY.GDP.PCAP.KD` | Economic productivity |
| Total Population | `SP.POP.TOTL` | National population |
| Urban Population % | `SP.URB.TOTL.IN.ZS` | Urbanization level |
| Energy Use per Capita | `EG.USE.PCAP.KG.OE` | Energy demand indicator |

---

## 🛠 Tools Used

- Python (Jupyter Notebook via Anaconda)
- `pandas`, `scikit-learn`, `matplotlib`, `seaborn`
- Visualizations: heatmaps, scatter plots

---

## 📸 Visuals

### 🔥 Correlation Heatmap  
![correlation](images/correlation.png)

### 📈 Actual vs Predicted (Random Forest)  
![actual_vs_predicted](images/actual_vs_predicted.png)

---

## ⚖️ Ethical Considerations

- Some countries have incomplete or outdated data.
- Emission forecasting is only as fair as the indicators allow.
- The model can support fairer and more sustainable transport strategies.

---

## 💡 Future Work

- Use **Streamlit** to deploy an interactive CO₂ forecast tool  
- Add more features: fuel prices, vehicle registration, traffic data  
- Evaluate region-specific models (Africa, Asia, Europe)

---

## 🧪 Run It Yourself

1. Clone this repo
2. Open Jupyter Notebook
3. Run `notebook.ipynb`

Requirements:
```bash
pip install pandas scikit-learn matplotlib seaborn
