# SDG3: Mental Health & Global Development Drivers

**Analytics Techniques and Tools | 2026**

Developed by **Atasha Marie M. Balictar**

---

## ⌕ Overview

Suicide mortality rates do not exist in isolation. They intersect with economic conditions, digital access, healthcare affordability, and urban development. This dashboard examines these connections across 266 countries from 2010 to 2021.

The analysis focuses on five key indicators: internet usage, unemployment, out-of-pocket health expenditure, urban population, and their relationships with suicide rates.

---

## ❒ Dataset Information

This project leverages an integrated dataset combining global mental health tracking metrics with key developmental drivers spanning multiple years.

* **Target Variable:** Suicide Rate (per 100,000 population)
* **Unit of Analysis:** Country-level records grouped globally
* **Features Matrix (Independent Variables):**
  * `Unemployment Rate` (% of Labor Force)
  * `Internet Usage` (%)
  * `Out-of-Pocket Health Expenditure` (% of Total Health Spend)
  * `Urban Population Percentage` (% of Total)
* **Data Sourcing:** Suicide Mortality Rate dataset sourced from the World Bank (Indicator: `SH.STA.SUIC.P5`), originally compiled via the WHO Global Health Observatory.
  
---

## ❏ Features of the Dashboard

### ⿻ Longitudinal & Bivariate Analysis
* **Dynamic Time Series:** Tracks structural country and global trajectories across selective macro targets with custom-filtered year spans.
* **Interactive Bivariate Engine:** Dropdown configurations running real-time Pearson correlation evaluations between economic factors and health metrics.

### 🗠 Predictive Intelligence
* **Trend Forecasting Module:** Employs linear regression modeling to calculate and graph statistical trajectory projections for specific countries from 2022 out through 2030.
* **Global Predictive Matrix:** Integrated Multiple Linear Regression (OLS) diagnostics engine showcasing systemic parameter values ($β$), $t$-values, and significance metrics ($p$-values) simultaneously.

### 🗐 Raw Data Explorer
* **Granular Filtering & Inspection:** Features multi-column isolation and dynamic country matching, backed by an embedded statistical summary extractor and a localized CSV downloader.

---

## ❒ Technologies Used

* **Language Platform:** Python
* **Frontend Interface:** Streamlit (Custom Dark-Minimalist HTML/CSS Component Architecture)
* **Data Engineering Engine:** Pandas & NumPy
* **Statistical Modeling Backend:** SciPy Stats (Linear Regression Tracking) & Statsmodels (OLS Matrix Engine)
* **Interactive Visualizations:** Plotly Express & Plotly Graph Objects
* **Static Graphics Processing:** Matplotlib & Seaborn (Matrix Visualization Engine)

---

## ❏ Live Dashboard

⤷ [View the Live Analytics Dashboard](https://sdg3-mental-health-analytics.streamlit.app/) 

