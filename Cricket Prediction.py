import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder

# Step 1: Simulate Raw Data (Web Scraping)
players_data = [
    {"name": "Sachin Tendulkar", "matches": 664, "runs": 34357, "wickets": 201, "country": "India", "role": "Batsman", "success": 1},
    {"name": "Rahul Dravid", "matches": 509, "runs": 24208, "wickets": 4, "country": "India", "role": "Batsman", "success": 1},
    {"name": "Suryakumar Yadav", "matches": 534, "runs": 17966, "wickets": 0, "country": "India", "role": "Batsman", "success": 0},
    {"name": "Ravichandran Ashwin", "matches": 788, "runs": 4000, "wickets": 704, "country": "India", "role": "All-Rounder", "success": 1},
    {"name": "Jasprit Bumrah", "matches": 624, "runs": 1000, "wickets": 297, "country": "India", "role": "Bowler", "success": 1}
]
df_raw = pd.DataFrame(players_data)

# Step 2: Data Cleaning
df_raw.fillna(0, inplace=True)

# Step 3: Feature Engineering
df_raw['batting_avg'] = df_raw['runs'] / df_raw['matches']
df_raw['bowling_eff'] = df_raw['wickets'] / df_raw['matches']
encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(df_raw[['role', 'country']])
feature_names = encoder.get_feature_names_out(['role', 'country'])
encoded_df = pd.DataFrame(encoded, columns=feature_names)
df = pd.concat([df_raw, encoded_df], axis=1).drop(columns=['role', 'country'])

# Step 4: Self-Training
X = df.drop(columns=["name", "success"])
y = df["success"]
class_0 = y[y == 0].index[:1]
class_1 = y[y == 1].index[:1]
labeled_idx = class_0.union(class_1)
unlabeled_idx = y.index.difference(labeled_idx)

X_labeled = X.loc[labeled_idx]
y_labeled = y.loc[labeled_idx]
X_unlabeled = X.loc[unlabeled_idx]

base_model = LogisticRegression()
base_model.fit(X_labeled, y_labeled)
pseudo_labels = base_model.predict(X_unlabeled)

X_combined = pd.concat([X_labeled, X_unlabeled])
y_combined = pd.concat([y_labeled, pd.Series(pseudo_labels, index=X_unlabeled.index)])

# Step 5: Supervised Fine-Tuning
model = RandomForestClassifier()
model.fit(X_combined, y_combined)

# Step 6: Simulated RLHF
feedback = (model.predict(X_combined) != y_combined).astype(int)
y_improved = y_combined.copy()
y_improved[feedback == 1] = 1
model.fit(X_combined, y_improved)

# Final prediction
df['predicted_success_probability'] = model.predict_proba(X)[:, 1]

# Show results
print(df[['name', 'predicted_success_probability']])

from transformers import pipeline
import pandas as pd

# Simulated real comments
players = [
    {
        "name": "Sachin Tendulkar",
        "fan_comments": [
            "Sachin is the greatest batsman of all time!",
            "Master Blaster never fails to inspire.",
            "His legacy will live on forever."
        ],
        "expert_comments": [
            "No player has matched Sachin's consistency and grace.",
            "An icon whose records remain untouched."
        ]
    },
    {
        "name": "Suryakumar Yadav",
        "fan_comments": [
            "SKY plays innovative shots but lacks consistency sometimes.",
            "His T20 form is amazing, hope he does well in Tests too."
        ],
        "expert_comments": [
            "Exciting talent, needs more exposure at the international level.",
            "A player to watch if he can adjust to swing bowling."
        ]
    }
]

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(comments):
    results = sentiment_pipeline(comments)
    scores = [1 if r['label'] == 'POSITIVE' else -1 for r in results]
    return sum(scores) / len(scores)

# Aggregate sentiment
results = []
for player in players:
    fan_score = analyze_sentiment(player['fan_comments'])
    expert_score = analyze_sentiment(player['expert_comments'])
    avg_score = round((fan_score + expert_score) / 2, 2)

    sentiment_label = "positive" if avg_score > 0.3 else "neutral" if avg_score > -0.3 else "negative"
    
    results.append({
        "name": player['name'],
        "fan_sentiment": round(fan_score, 2),
        "expert_sentiment": round(expert_score, 2),
        "avg_sentiment_score": avg_score,
        "predicted_sentiment": sentiment_label
    })

# View as DataFrame
df = pd.DataFrame(results)
print(df)