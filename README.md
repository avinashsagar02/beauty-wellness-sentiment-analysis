# Beauty & Wellness Customer Sentiment & Feedback Analysis

[![Internship Track](https://img.shields.io/badge/Internship-Data%20Science%20with%20Python-blue.svg)](https://github.com)
[![Deliverable](https://img.shields.io/badge/Deliverable-Week%202%20Task-green.svg)](https://github.com)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)

## Project Overview
This repository contains the research, data sourcing strategy, and exploratory data analysis (EDA) pipeline for analyzing customer sentiment, product efficacy, and feedback patterns in the **Beauty and Personal Care E-Commerce sector**.

While aggregate star ratings (1 to 5 stars) provide broad indicators of satisfaction, they fail to isolate underlying defect drivers—such as chemical allergies, formulation breakouts, and dispensing pump malfunctions. This project builds an automated Natural Language Processing (NLP) framework to extract actionable customer insights from unstructured consumer reviews.

---

## Week 2 Objectives & Scope
- **Data Identification & Sourcing:** Systematic audit of public beauty review corpora (Sephora Kaggle Dataset, Amazon Customer Reviews, Reddit APIs).
- **Quality & Hygiene Audit:** Protocols to address demographic sparsity, promotional spam, and the natural 5-star positivity skew.
- **Worked Exploratory Data Analysis (EDA):** Modular Python implementation performing regex text sanitization, custom cosmetic stopword removal, and N-gram frequency modeling.
- **Statistical Hypothesis Testing:** Formulating Chi-Square and Two-Sample t-tests to evaluate adverse dermal reactions and review verbosity polarities.

---

## Repository Structure
```text
├── README.md               # Complete project documentation & sourcing strategy
├── eda_script.py           # Python script for text preprocessing, EDA, and N-gram extraction
└── requirements.txt        # Python package dependencies
