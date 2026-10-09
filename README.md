# ☀️ AI-Based Heatwave Monitoring and Early Warning System
> **Academic Year 2026–27 | S.Y. B.Tech Engineering**  
> **Course:** Statistical Methods and Probability (SMP) | **Internal Assessment – IA 1**  
> **Theme:** STAT-AI Engineering Challenge — *From Data to Decision*  
> **Case Study 1:** AI-Based Heatwave Monitoring and Early Warning (Groups 1–4)

---

## 📌 Executive Summary
Extreme heatwaves pose catastrophic risks to public health, municipal water infrastructure, and power grids across urban India. Conventional weather systems rely on delayed retrospective reporting.  
This project presents an end-to-end **AI-Supported Statistical Early Warning Web Application** designed for real-time risk assessment using telemetry from the India Meteorological Department (IMD). The system executes the core engineering paradigm:

$$\textbf{Input/Data} \longrightarrow \textbf{Statistical Method} \longrightarrow \textbf{Result} \longrightarrow \textbf{Engineering/AI Decision}$$

---

## 🏗️ System Architecture & Pipeline

```mermaid
flowchart LR
    A[IMD Weather Telemetry\nN=65 Daily Observations] --> B[Data Hygiene & IQR Outliers\nClass Intervals & Ogive Curves]
    B --> C[Descriptive Dispersion\nMean, Variance, CV = 8.18%]
    C --> D[Gaussian Fitting & Z-Scores\nP(T ≥ 40°C) & P(T ≥ 42°C)]
    D --> E[Bayesian Inference\nP(Heatwave | IoT Sensor Alert)]
    E --> F[Random Process & ACF\nThermal Memory Lag-1 = 0.77]
    F --> G[Rule-Based AI Engine\nGreen | Yellow | Orange | Red Alert]
    G --> H[Actionable Municipal Directives\nHospitals, Water Tankers, Labor Shifts]
```

---

## ✨ Key Features

1. **Strictly Compliant with Evaluation Guidelines**:
   - **No PPT Needed**: Built for the live **6–7 minute Interactive Statistics Innovation Showcase**.
   - **Step-by-Step Mathematical Derivations**: Shows exact LaTeX formulas and numerical substitutions for every metric alongside code output.
2. **Interactive What-If Simulation Engine**:
   - Dynamic sidebar sliders allow evaluators to test hypothetical temperature spikes ($\Delta T$) and relative humidity shifts to observe real-time transitions in warning levels.
3. **Decoupled Modular Architecture**:
   - Built into 6 dedicated Python modules corresponding to 6 distinct team roles, preventing merge conflicts and ensuring clear individual ownership.
4. **Rich Interactive Plotly Visualizations**:
   - Continuous Frequency Histograms & Cumulative Frequency Ogive curves.
   - Box-and-Whisker dispersion diagrams.
   - Normal Distribution Bell Curve with shaded critical tail exceedance areas.
   - 2D Joint Density Heatmap (Temperature vs Relative Humidity).
   - Sample Autocorrelation Function (ACF) Correlogram with 95% Bartlett confidence bands.
5. **One-Click Official Report Exporter**:
   - Generates the complete 2–3 page Statistical Investigation Sheet in text format for instant submission.

---

## 👥 6-Member Work Division & Syllabus Allocation

| Member | Designated Role | Module File | Syllabus Topic & Contribution | Presentation Slot |
| :---: | :--- | :--- | :--- | :---: |
| **Member 1** | **Data Engineering Lead** | `modules/data_loader.py` | Sourcing IMD data, IQR outlier removal, 7-bin continuous frequency distribution table, and Ogive curve. | Min 0:00 – 1:00 |
| **Member 2** | **Descriptive Statistics Lead** | `modules/descriptive_stats.py` | Central tendency ($\bar{x}, M_d, M_o$), variance ($s^2$), standard deviation ($s$), and Coefficient of Variation ($CV$). | Min 1:00 – 2:00 |
| **Member 3** | **Probability & Extreme Value Lead** | `modules/extreme_value_analysis.py` | Fitting Gaussian distribution $\mathcal{N}(\mu, \sigma^2)$, $Z$-scores, tail exceedance probabilities ($P(T \ge 40^\circ\text{C})$). | Min 2:00 – 3:15 |
| **Member 4** | **Bayesian Inference Specialist** | `modules/bayesian_inference.py` | Joint/Marginal contingency tables, conditional probability $P(\text{Heatwave} \mid \text{High Hum})$, and Bayes' Theorem for sensor updates. | Min 3:15 – 4:30 |
| **Member 5** | **Time Series & Random Process Lead** | `modules/time_series_process.py` | Temperature as a discrete random process $\{X_t\}$, sample autocorrelation ($r_1$ to $r_7$), stationarity, and streak detection. | Min 4:30 – 5:30 |
| **Member 6** | **AI Decision Engine & UI Lead** | `modules/decision_engine.py` & `app.py` | Rule-based AI Early Warning System (Green/Yellow/Orange/Red), municipal directives, What-If simulation, and UI coordination. | Min 5:30 – 6:45 |

---

## 📁 Repository Directory Structure

```
d:\SMP maths app\
├── .gitignore                          # Clean Python gitignore
├── README.md                           # Project documentation & GitHub guide
├── requirements.txt                    # Project dependencies
├── app.py                              # Main Streamlit Interactive Application
├── data/
│   ├── imd_heatwave_mumbai_maharashtra.csv  # Verified IMD summer temperature dataset (N=65)
│   └── sample_upload_template.csv     # Template for custom dataset uploads
├── modules/
│   ├── __init__.py
│   ├── data_loader.py                  # Member 1: Ingestion & Frequency Tables
│   ├── descriptive_stats.py            # Member 2: Central Tendency & Dispersion
│   ├── extreme_value_analysis.py       # Member 3: Gaussian Fitting & Z-Scores
│   ├── bayesian_inference.py           # Member 4: Conditional Probability & Bayes
│   ├── time_series_process.py          # Member 5: Random Process & Autocorrelation
│   └── decision_engine.py              # Member 6: Rule-Based AI Decision Matrix
└── docs/
    ├── STATISTICAL_INVESTIGATION_SHEET.md   # Official 2-3 page assessment submission sheet
    ├── PRESENTATION_SCRIPT_AND_VIVA_PREP.md # Timed 6-7 min showcase script + 30 viva Q&As
    └── TEAM_WORK_DIVISION.md           # Detailed Git workflow and milestone checklist
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure Python 3.10+ is installed on your machine.

### 2. Clone the Repository
```bash
git clone <YOUR_GITHUB_REPO_URL>
cd "SMP maths app"
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the Interactive Web Application
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501`.

---

## 📊 Evaluation Scheme Coverage (Total: 20 Marks)

| Evaluation Criteria | Marks | How This Project Satisfies It |
| :--- | :---: | :--- |
| **Statistical Concepts & Mathematical Correctness** | **5** | Formal derivations with formulas and substituted numerical values in every tab. |
| **Dataset, Calculations & Statistical Analysis** | **4** | Authentic 65-observation IMD dataset, frequency tables, and step-by-step calculations. |
| **Interactive Working Demonstration** | **5** | Live Streamlit app with interactive threshold sliders and real-time alert triggers. |
| **Graphical Representation & Interpretation** | **2** | Plotly histograms, Ogive curves, box plots, Gaussian PDF bell curves, heatmaps, and ACF plots. |
| **AI/Engineering Application & Decision** | **2** | Multi-tier AI Early Warning Engine issuing explicit hospital and municipal directives. |
| **Individual Viva & Participation** | **2** | 6 distinct presentation slots and a 30-question viva preparation guide for all members. |
| **Total** | **20** | **Complete coverage across all rubric items.** |

---

## 📜 References
- India Meteorological Department (IMD), *Criteria for Declaring Heat Wave and Severe Heat Wave in India*, Government of India.
- National Disaster Management Authority (NDMA), *National Guidelines for Management of Heat Wave*.
- National Oceanic and Atmospheric Administration (NOAA), *The Heat Index Equation*.
