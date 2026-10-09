# 👥 6-Member Team Work Division & Git Workflow Guide
## Academic Year 2026–27 | Statistical Methods and Probability (IA-1)
### Case Study 1: AI-Based Heatwave Monitoring and Early Warning System

---

## 📋 Member Task Allocation & Module Ownership

| Member | Designated Role | Core Code Module | Presentation Slot | Deliverables Checklist |
| :---: | :--- | :--- | :---: | :--- |
| **Member 1** | **Data Engineering & Ingestion Lead** | `modules/data_loader.py` | Min 0:00 – 1:00 | - Verify dataset has 60+ observations.<br>- Implement IQR outlier detection.<br>- Build continuous frequency table with 7 bins.<br>- Explain data hygiene in presentation. |
| **Member 2** | **Descriptive Statistics Lead** | `modules/descriptive_stats.py` | Min 1:00 – 2:00 | - Compute Mean, Median, Mode.<br>- Compute Variance, Standard Deviation, CV.<br>- Verify grouped vs ungrouped calculations.<br>- Explain thermal volatility in presentation. |
| **Member 3** | **Probability & Extreme Value Lead** | `modules/extreme_value_analysis.py` | Min 2:00 – 3:15 | - Fit Gaussian Normal Distribution $\mathcal{N}(\mu, \sigma^2)$.<br>- Calculate $Z$-scores for 40°C, 42°C, 45°C.<br>- Implement shaded tail area Plotly graph.<br>- Demonstrate threshold slider in presentation. |
| **Member 4** | **Bayesian Inference Specialist** | `modules/bayesian_inference.py` | Min 3:15 – 4:30 | - Build Joint & Marginal frequency cross-tabs.<br>- Compute conditional probability $P(\text{Heatwave} \mid \text{High Hum})$.<br>- Implement Bayes' Theorem for IoT sensor alerts.<br>- Explain false-alarm filtering in presentation. |
| **Member 5** | **Time Series & Random Process Lead** | `modules/time_series_process.py` | Min 4:30 – 5:30 | - Compute Autocorrelation coefficients $r_1$ to $r_7$.<br>- Plot correlogram with 95% Bartlett bounds.<br>- Implement 7-day rolling stationarity check.<br>- Detect multi-day heatwave streaks. |
| **Member 6** | **AI Decision Engine & UI Lead** | `modules/decision_engine.py` & `app.py` | Min 5:30 – 6:45 | - Implement IMD Green/Yellow/Orange/Red alert logic.<br>- Connect interactive What-If sliders to decision cards.<br>- Coordinate Streamlit UI and GitHub repository.<br>- Lead live simulation during the presentation. |

---

## 🌿 Git Branching Strategy & Collaboration

To avoid code conflicts, each member works on their own feature branch:

```
main (Production Branch)
 ├── feature/m1-data-pipeline       (Member 1)
 ├── feature/m2-descriptive-stats   (Member 2)
 ├── feature/m3-normal-distribution (Member 3)
 ├── feature/m4-bayesian-inference  (Member 4)
 ├── feature/m5-time-series-acf     (Member 5)
 └── feature/m6-decision-engine-ui  (Member 6)
```

### Git Command Cheatsheet for Team Members:

1. **Clone the repository:**
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd "SMP maths app"
   ```

2. **Create and switch to your feature branch:**
   ```bash
   # Member 1:
   git checkout -b feature/m1-data-pipeline

   # Member 2:
   git checkout -b feature/m2-descriptive-stats

   # Member 3:
   git checkout -b feature/m3-normal-distribution

   # Member 4:
   git checkout -b feature/m4-bayesian-inference

   # Member 5:
   git checkout -b feature/m5-time-series-acf

   # Member 6:
   git checkout -b feature/m6-decision-engine-ui
   ```

3. **Stage, commit, and push your changes:**
   ```bash
   git add .
   git commit -m "feat(module): implement calculations and tests for Member X"
   git push origin <YOUR_BRANCH_NAME>
   ```

4. **Merge into main branch (Team Lead):**
   ```bash
   git checkout main
   git merge <FEATURE_BRANCH_NAME>
   git push origin main
   ```

---

## 🚀 How to Run the Web Application Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch Streamlit App:**
   ```bash
   streamlit run app.py
   ```
   *The application will open in your browser at `http://localhost:8501`.*
