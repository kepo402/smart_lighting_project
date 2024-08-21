import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import os
import random
import pickle

# Get the absolute path of the project directory
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Construct the absolute path for the CSV file
data_path = os.path.join(project_dir, 'data', 'simulated_data.csv')

# Read the data from the CSV file
df = pd.read_csv(data_path)

# Simulate preferred light levels based on light level and occupancy
df['preferred_light_level'] = df['light_level'] * 0.5 + df['occupancy'] * 100 + random.uniform(-50, 50)

# Define features and target variable
X = df[['light_level', 'occupancy']]
y = df['preferred_light_level']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForestRegressor model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model performance
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model training complete.")
print(f"Mean Absolute Error on test set: {mae}")
print(f"R^2 Score on test set: {r2}")

# Save the model for later use
model_path = os.path.join(project_dir, 'src', 'model', 'model.pkl')
os.makedirs(os.path.dirname(model_path), exist_ok=True)
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

# Test with new data
new_data = pd.DataFrame({
    'light_level': [200, 400],
    'occupancy': [1, 0]
})
new_predictions = model.predict(new_data)
print(f"Predictions for new data:\n{new_predictions}")
