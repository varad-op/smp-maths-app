# STATISTICAL INVESTIGATION SHEET
## Academic Year 2026–27 | S.Y. B.Tech Engineering
### Course: Statistical Methods and Probability (SMP) | Internal Assessment – IA 1
**Theme:** STAT-AI Engineering Challenge — *From Data to Decision*  
**Case Study 1:** AI-Based Heatwave Monitoring and Early Warning System  
**Submission Format:** `GroupNumber_TopicName_StatAI_IA1`  
**Evaluation Marks:** 20 Marks (Mode: Interactive Demonstration & Viva)

---

## 1. Problem Statement
Heatwaves represent one of the most hazardous meteorological extremes in India, leading to heat strokes, agricultural stress, municipal water strain, and electrical power grid surges. Conventional monitoring often relies on retrospective or isolated daily alerts.  
The engineering objective is to design an **AI-Supported Statistical Early Warning System** that continuously ingests daily temperature and humidity telemetry, performs rigorous descriptive and inferential statistical modeling, and automatically transitions between municipal action levels (**Green, Yellow, Orange, Red**) to enable pre-emptive disaster mitigation.

---

## 2. Description of the Dataset
- **Source of Data:** India Meteorological Department (IMD) / Open Government Data Platform India (`data.gov.in`) & NASA POWER Meteorological API.
- **Geographic Focus:** Mumbai & Vidarbha Region, Maharashtra, India.
- **Observation Count ($N$):** 65 daily sequential observations covering the pre-monsoon summer spell (March 15 to May 18, 2026).
- **Recorded Variables:**
  1. `Date`: Chronological date sequence (`YYYY-MM-DD`).
  2. `Max_Temp_C`: Daily maximum surface air temperature ($^\circ\text{C}$).
  3. `Min_Temp_C`: Daily minimum surface air temperature ($^\circ\text{C}$).
  4. `Relative_Humidity_Pct`: Afternoon relative humidity ($\%$).
  5. `Heat_Index_C`: NOAA Apparent Temperature calculated via the Rothfusz polynomial ($^\circ\text{C}$).
  6. `Weather_Condition`: Categorical classification (`Normal`, `Moderate Heat`, `Heatwave`, `Severe Heatwave`).

---

## 3. Statistical Concepts Used & Relevant Formulae

### A. Data Hygiene & Outlier Detection (IQR Method)
- First Quartile ($Q_1$): $25^{\text{th}}$ percentile; Third Quartile ($Q_3$): $75^{\text{th}}$ percentile.
- Interquartile Range:
  $$\text{IQR} = Q_3 - Q_1$$
- Inner Fences:
  $$\text{Lower Bound} = Q_1 - 1.5 \times \text{IQR}, \quad \text{Upper Bound} = Q_3 + 1.5 \times \text{IQR}$$

### B. Measures of Central Tendency & Dispersion
- **Sample Mean ($\bar{x}$):**
  $$\bar{x} = \frac{\sum_{i=1}^N x_i}{N}$$
- **Sample Variance ($s^2$) & Standard Deviation ($s$):**
  $$s^2 = \frac{\sum_{i=1}^N (x_i - \bar{x})^2}{N - 1}, \quad s = \sqrt{s^2}$$
- **Coefficient of Variation ($CV$):**
  $$CV = \left( \frac{s}{\bar{x}} \right) \times 100\%$$
- **Grouped Mean:**
  $$\bar{x}_{\text{grouped}} = \frac{\sum f_i x_i}{\sum f_i}$$

### C. Extreme Temperature Modeling (Gaussian / Normal Distribution)
Assuming $X \sim \mathcal{N}(\mu, \sigma^2)$:
- **Standard Normal Variable ($Z$):**
  $$Z = \frac{X - \mu}{\sigma}$$
- **Tail Exceedance Probability ($P(X \ge T)$):**
  $$P(X \ge T) = 1 - \Phi(Z) = \int_{T}^\infty \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}\left( \frac{x-\mu}{\sigma} \right)^2} dx$$

### D. Joint & Conditional Probability and Bayesian Inference
- **Conditional Probability:**
  $$P(\text{Heatwave} \mid \text{High Humidity}) = \frac{n(\text{Heatwave} \cap \text{High Humidity})}{n(\text{High Humidity})}$$
- **Bayes' Theorem for IoT Weather Sensor Alarm:**
  $$P(H \mid S) = \frac{P(S \mid H) \cdot P(H)}{P(S \mid H) \cdot P(H) + P(S \mid \neg H) \cdot P(\neg H)}$$
  Where $H$ is true heatwave state and $S$ is sensor alarm trigger.

### E. Discrete Random Process & Autocorrelation
- **Sample Autocorrelation Function (ACF):**
  $$r_k = \frac{\sum_{t=1}^{N-k} (X_t - \bar{x})(X_{t+k} - \bar{x})}{\sum_{t=1}^N (X_t - \bar{x})^2}, \quad k \in \{1, 2, \dots, 7\}$$
- **95% Confidence Bounds:**
  $$\text{CI}_{95\%} = \pm \frac{1.96}{\sqrt{N}}$$

---

## 4. Step-by-Step Numerical Calculations

### Calculation 1: Descriptive Statistics
For $N = 65$ observations of Maximum Temperature ($T_{\max}$):
- $\sum_{i=1}^{65} x_i = 2439.40^\circ\text{C}$
- Mean:
  $$\bar{x} = \frac{2439.40}{65} = 37.53^\circ\text{C}$$
- Median: $M_d = 37.30^\circ\text{C}$
- $\sum (x_i - \bar{x})^2 = 476.12$
- Variance:
  $$s^2 = \frac{476.12}{65 - 1} = \frac{476.12}{64} = 7.4393\ (^\circ\text{C})^2$$
- Standard Deviation:
  $$s = \sqrt{7.4393} = 2.73^\circ\text{C}$$
- Coefficient of Variation:
  $$CV = \left( \frac{2.73}{37.53} \right) \times 100\% = 7.27\%$$

### Calculation 2: Continuous Frequency Distribution (7 Structured Bins)
| Class Interval ($^\circ\text{C}$) | Class Mark ($x_i$) | Frequency ($f_i$) | Cumulative Freq ($cf$) | Relative Freq ($\%$) | $f_i x_i$ | $f_i x_i^2$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 31.0 – 33.0 | 32.0 | 3 | 3 | 4.62% | 96.00 | 3,072.00 |
| 33.0 – 35.0 | 34.0 | 6 | 9 | 9.23% | 204.00 | 6,936.00 |
| 35.0 – 37.0 | 36.0 | 17 | 26 | 26.15% | 612.00 | 22,032.00 |
| 37.0 – 39.0 | 38.0 | 23 | 49 | 35.38% | 874.00 | 33,212.00 |
| 39.0 – 41.0 | 40.0 | 10 | 59 | 15.38% | 400.00 | 16,000.00 |
| 41.0 – 43.0 | 42.0 | 2 | 61 | 3.08% | 84.00 | 3,528.00 |
| 43.0 – 45.0 | 44.0 | 4 | 65 | 6.15% | 176.00 | 7,744.00 |
| **Total** | — | **$N = 65$** | — | **100.00%** | **2,446.00** | **92,524.00** |

- Grouped Mean:
  $$\bar{x}_{\text{grouped}} = \frac{\sum f_i x_i}{\sum f_i} = \frac{2446.00}{65} = 37.63^\circ\text{C}$$
- Grouped Median: Median Class = $[37.0 - 39.0]$, $L = 37.0$, $N/2 = 32.5$, $cf_{\text{prev}} = 26$, $f = 23$, $h = 2.0$:
  $$M_d = 37.0 + \left[ \frac{32.5 - 26}{23} \right] \times 2.0 = 37.0 + 0.565 = 37.57^\circ\text{C}$$
- Discretization discrepancy: $\Delta = +0.10^\circ\text{C}$ ($0.27\%$), demonstrating robust continuous bin fidelity.

### Calculation 3: Extreme Value Probability via Normal Distribution
Fitting $\mathcal{N}(\mu = 37.53^\circ\text{C}, \sigma = 2.73^\circ\text{C})$:
- **Threshold $T = 38.0^\circ\text{C}$ (Heat Watch Advisory):**
  $$Z_{38} = \frac{38.0 - 37.53}{2.73} = +0.1722 \implies P(X \ge 38.0^\circ\text{C}) = 1 - \Phi(0.17) = 43.17\%$$
- **Threshold $T = 40.0^\circ\text{C}$ (Official IMD Heatwave Alert):**
  $$Z_{40} = \frac{40.0 - 37.53}{2.73} = +0.9048 \implies P(X \ge 40.0^\circ\text{C}) = 1 - \Phi(0.90) = 18.28\%$$
- **Threshold $T = 42.0^\circ\text{C}$ (Severe Heatwave Emergency):**
  $$Z_{42} = \frac{42.0 - 37.53}{2.73} = +1.6374 \implies P(X \ge 42.0^\circ\text{C}) = 1 - \Phi(1.64) = 5.08\%$$
- **Threshold $T = 45.0^\circ\text{C}$ (Catastrophic Outlier):**
  $$Z_{45} = \frac{45.0 - 37.53}{2.73} = +2.7363 \implies P(X \ge 45.0^\circ\text{C}) = 1 - \Phi(2.74) = 0.31\%$$

### Calculation 4: Contingency Matrix & Bayesian Sensor Update
- Historical Prior Heatwave Probability: $P(H) = 7/65 = 0.1077\ (10.77\%)$
- Prior Non-Heatwave: $P(\neg H) = 58/65 = 0.8923\ (89.23\%)$
- Sensor True Positive Rate: $P(S \mid H) = 0.92$
- Sensor False Alarm Rate: $P(S \mid \neg H) = 0.08$
- Marginal Sensor Alert Probability:
  $$P(S) = (0.92 \times 0.1077) + (0.08 \times 0.8923) = 0.0991 + 0.0714 = 0.1705$$
- Posterior Probability via Bayes' Theorem:
  $$P(H \mid S) = \frac{P(S \mid H) \cdot P(H)}{P(S)} = \frac{0.0991}{0.1705} = 0.5812\ (58.12\%)$$
- *Engineering Takeaway:* IoT sensor alarms elevate belief from baseline $10.77\%$ to $58.12\%$, successfully filtering $41.88\%$ of false emergency calls before dispatching municipal resources.

### Calculation 5: Autocorrelation & Random Process
- Number of observations $N = 65 \implies \text{Bartlett 95% Confidence Bound} = \pm \frac{1.96}{\sqrt{65}} = \pm 0.2431$
- Autocorrelation Coefficients:
  - $r_1 = +0.9026$ (Statistically significant, $\gg +0.2431$)
  - $r_2 = +0.8050$ (Statistically significant)
  - $r_3 = +0.6862$ (Statistically significant)
  - $r_4 = +0.5291$ (Statistically significant)
  - $r_5 = +0.3717$ (Statistically significant)
  - $r_6 = +0.1926$ (Insignificant, memory within noise)
  - $r_7 = +0.0455$ (Insignificant)
- Heatwave Streak: Detected continuous 6-day streak (May 4 to May 9, 2026) peaking at $44.40^\circ\text{C}$.
- *Inference:* Atmospheric thermal memory persists up to 5 days, confirming heatwaves act as autocorrelated multi-day spells rather than memoryless noise.

---

## 5. AI / Engineering Decision Matrix
Based on synthesized statistical inputs, the system triggers official disaster responses:

| Alert Level | Trigger Condition | Statistical Indicator | Mandated Engineering / Civil Action |
| :---: | :---: | :---: | :--- |
| **GREEN** | $T < 38^\circ\text{C}$ | $P(T \ge 40) < 15\%$ | Routine meteorological logging; normal municipal operations. |
| **YELLOW** | $38^\circ\text{C} \le T < 40^\circ\text{C}$ | $P(T \ge 40) \in [15\%, 35\%)$ | Public health warnings; pre-position water tankers; hospital hydration stations. |
| **ORANGE** | $40^\circ\text{C} \le T < 42^\circ\text{C}$ OR Streak $\ge 2$ days | $P(T \ge 40) \ge 40\%$ OR $P(H \mid S) > 80\%$ | Primary school afternoon closures; halt outdoor construction 12:00–3:30 PM; standby ORS beds. |
| **RED** | $T \ge 42^\circ\text{C}$ OR Heat Index $\ge 50^\circ\text{C}$ | $P(T \ge 42) \ge 35\%$ | Emergency heatstroke ICU activation; grid spinning reserve ramp-up; municipal emergency broadcasts. |

---

## 6. Limitations of the Statistical Model
1. **Gaussian Distribution Assumption:** While temperatures generally follow a bell shape, extreme heat events possess asymmetric right-tail skewness (extreme value Frechet/Gumbel distribution provides higher tail fidelity).
2. **Stationarity Bounds:** Meteorological processes are non-stationary across season transitions (e.g., transition from pre-monsoon dry heat to monsoonal humidity).
3. **Microclimate Variations:** Urban Heat Island (UHI) effects cause localized asphalt temperature variances not captured by a single regional meteorological station.

---

## 7. References
1. India Meteorological Department (IMD), *Criteria for Declaring Heat Wave and Severe Heat Wave in India*, Government of India.
2. National Disaster Management Authority (NDMA), *National Guidelines for Preparation of Action Plan - Prevention and Management of Heat Wave*.
3. National Oceanic and Atmospheric Administration (NOAA), *The Heat Index Equation and Rothfusz Regression*, National Weather Service.
