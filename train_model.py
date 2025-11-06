import pandas as pd
import pickle
from sklearn.tree import DecisionTreeClassifier
import numpy as np

df = pd.read_csv('dataset/nutrition_dataset.csv')
print('Dataset shape:', df.shape)
print('Column names:')
print(df.columns.tolist())
print('\nFirst few rows:')
print(df.head())

# Prepare features and target
feature_names = ['Age', 'Gender', 'BMI', 'Health', 'Allergy', 'Preference']
X = df[feature_names]
y = df['Diet']

# Train the model
model = DecisionTreeClassifier(random_state=42, max_depth=5)
model.fit(X, y)

# Save the model and feature names
with open('model/diet_model.pkl', 'wb') as f:
    pickle.dump({'model': model, 'feature_names': feature_names}, f)

print('\nModel trained and saved successfully!')
