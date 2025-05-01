import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Step 1: Generate sample data
# y = 3x + 5 + noise
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 3 * X + 5 + np.random.randn(100, 1)

# Step 2: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 3: Save model to a pickle file
with open("linear_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved to linear_model.pkl")
