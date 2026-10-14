# Beauty & Wellness Customer Sentiment & Feedback Analysis

[![Internship Track](https://img.shields.io/badge/Internship-Data%20Science%20with%20Python-blue.svg)](https://github.com)
[![Deliverable](https://img.shields.io/badge/Deliverable-Week%202%20Task-green.svg)](https://github.com)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)

## 📌 Project Overview
This repository contains the research, data sourcing strategy, and exploratory data analysis (EDA) pipeline for analyzing customer sentiment, product efficacy, and feedback patterns in the **Beauty and Personal Care E-Commerce sector**.

While aggregate star ratings (1 to 5 stars) provide broad indicators of satisfaction, they fail to isolate underlying defect drivers—such as chemical allergies, formulation breakouts, and dispensing pump malfunctions. This project builds an automated Natural Language Processing (NLP) framework to extract actionable customer insights from unstructured consumer reviews.

---

## 🎯 Week 2 Objectives & Scope
- **Data Identification & Sourcing:** Systematic audit of public beauty review corpora (Sephora Kaggle Dataset, Amazon Customer Reviews, Reddit APIs).
- **Quality & Hygiene Audit:** Protocols to address demographic sparsity, promotional spam, and the natural 5-star positivity skew.
- **Worked Exploratory Data Analysis (EDA):** Modular Python implementation performing regex text sanitization, custom cosmetic stopword removal, and N-gram frequency modeling.
- **Statistical Hypothesis Testing:** Formulating Chi-Square ($\chi^2$) and Two-Sample t-tests to evaluate adverse dermal reactions and review verbosity polarities.

---

## 📂 Repository Structure
```text
├── README.md               # Complete project documentation & sourcing strategy
├── eda_script.py           # Python script for text preprocessing, EDA, and N-gram extraction
└── requirements.txt        # Python package dependencies
```

---

## 📊 Data Sourcing & Repository Profiles

| Data Repository | Exact Scale | Features & Granularity | Strategic Utility |
| :--- | :--- | :--- | :--- |
| **Sephora Skincare Reviews (Kaggle)** | 8,000+ Products<br>1,000,000+ Reviews | `review_text`, `rating`, `skin_type`, `skin_tone`, `ingredients`, `verified_purchase` | **Primary Benchmark:** Directly maps biological skin traits to formulation reactions. |
| **Amazon Customer Reviews (Beauty - AWS)** | 30M+ Reviews<br>1M+ SKUs | `review_text`, `summary`, `verified_purchase`, `helpful_vote`, `unixTimestamp` | Scaled statistical baseline for generalizability across broader cosmetics categories. |
| **Reddit API (r/SkincareAddiction)** | 500k+ Threads & Comments | Conversational commentary, upvote scores, routine troubleshooting trees | Zero-commercial bias; ideal for emerging formulation discussions. |

---

## 🔬 Core Hypotheses Tested
- **Hypothesis 1 ($H_1$):** Negative reviews in leave-on skincare categories (serums, creams) are significantly more correlated with adverse dermal reactions (breakouts, redness) than mechanical or shipping defects.
- **Hypothesis 2 ($H_2$):** Extremely polarized customer reviews (1-star and 5-star ratings) demonstrate statistically greater descriptive verbosity (word count) compared to moderate 3-star reviews.

---

## 🚀 Getting Started & Execution

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/beauty-wellness-sentiment-analysis.git
cd beauty-wellness-sentiment-analysis
```

### 2. Install Dependencies
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### 3. Run the EDA Pipeline
```bash
python eda_script.py
```

---

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Data Engineering:** Pandas, NumPy
- **NLP & Feature Extraction:** Regular Expressions (`re`), Scikit-Learn (`CountVectorizer`, `TF-IDF`)
- **Statistical Testing:** SciPy (`scipy.stats`)
- **Visualizations:** Matplotlib, Seaborn
