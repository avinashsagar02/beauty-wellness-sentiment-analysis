"""
Beauty & Wellness Customer Sentiment & Feedback Analysis
Week 2: Exploratory Data Analysis & Preprocessing Pipeline
"""

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer

def clean_review_text(text, custom_stopwords=None):
    """
    Sanitize and normalize customer review text.
    - Strips HTML artifacts & punctuation
    - Converts to lower case
    - Filters custom domain filler stopwords
    """
    if not isinstance(text, str):
        return ""
    
    # Remove HTML tags & special characters
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    tokens = text.lower().split()
    
    if custom_stopwords:
        tokens = [t for t in tokens if t not in custom_stopwords and len(t) > 2]
        
    return ' '.join(tokens)

def run_eda_pipeline(data_path=None):
    print("=" * 60)
    print("Beauty & Wellness EDA Pipeline - Week 2 Analysis")
    print("=" * 60)
    
    # 1. Sample Data Loading (Simulated Sephora dataset if file not supplied)
    if data_path:
        df = pd.read_csv(data_path)
    else:
        print("[INFO] No dataset file provided. Creating synthetic validation corpus...")
        sample_records = [
            {"product_id": "P428230", "category": "Serum", "rating": 1, "skin_type": "Sensitive", 
             "review_text": "Gave me cystic acne along my jawline within 4 days. The pump also broke."},
            {"product_id": "P428230", "category": "Serum", "rating": 1, "skin_type": "Oily", 
             "review_text": "Severe allergic reaction and redness. Burning sensation on cheeks."},
            {"product_id": "P981244", "category": "Moisturizer", "rating": 5, "skin_type": "Dry", 
             "review_text": "Holy grail product! Deeply hydrating, smooth texture and absorbs instantly."},
            {"product_id": "P981244", "category": "Moisturizer", "rating": 5, "skin_type": "Normal", 
             "review_text": "Repurchased 3 times. Best barrier repair cream for winter dryness."},
            {"product_id": "P112349", "category": "Cleanser", "rating": 2, "skin_type": "Combination", 
             "review_text": "Leaves oily residue and clogged pores. Strong artificial perfume scent."},
            {"product_id": "P112349", "category": "Cleanser", "rating": 4, "skin_type": "Oily", 
             "review_text": "Gentle daily foaming cleanser. Decent value for money."}
        ]
        df = pd.DataFrame(sample_records)
    
    print(f"
[1] Dataset Shape: {df.shape[0]} reviews, {df.shape[1]} features")
    print("
[2] Numerical Rating Distribution:")
    print(df['rating'].describe())
    
    # 2. Text Normalization
    domain_stopwords = {'product', 'item', 'skin', 'use', 'using', 'used', 'really', 'would'}
    df['cleaned_text'] = df['review_text'].apply(lambda x: clean_review_text(x, custom_stopwords=domain_stopwords))
    df['word_count'] = df['review_text'].apply(lambda x: len(str(x).split()))
    
    # 3. Correlation & Hypothesis Metric (Polarized vs Moderate Length)
    df['is_extreme'] = df['rating'].apply(lambda r: 1 if r in [1, 5] else 0)
    mean_length = df.groupby('is_extreme')['word_count'].mean()
    print("
[3] Mean Word Count (Hypothesis 2 Check):")
    print(f"    - Extreme Reviews (1 & 5 Stars): {mean_length.get(1, 0):.2f} words")
    print(f"    - Moderate Reviews (2-4 Stars):  {mean_length.get(0, 0):.2f} words")
    
    # 4. Bigram Analysis for 1 & 2 Star Negative Reviews
    neg_reviews = df[df['rating'] <= 2]['cleaned_text'].tolist()
    if neg_reviews:
        vec = CountVectorizer(ngram_range=(2, 2), max_features=5)
        dtm = vec.fit_transform(neg_reviews)
        bigram_counts = pd.DataFrame(dtm.toarray(), columns=vec.get_feature_names_out()).sum()
        print("
[4] Top Recurring Negative Bigrams (Adverse Reactions vs Packaging):")
        print(bigram_counts.sort_values(ascending=False))
        
    print("
[INFO] EDA Pipeline Execution Completed Successfully.")
    return df

if __name__ == "__main__":
    run_eda_pipeline()
