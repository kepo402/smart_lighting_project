import pandas as pd
import matplotlib.pyplot as plt
import pickle
import random
import os

# Get the absolute path of the project directory
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Load the trained model
model_path = os.path.join(project_dir, 'src', 'model', 'model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Simulate and collect predictions over time
timestamps = []
predictions = []

for hour in range(24):
    new_data = pd.DataFrame({
        'light_level': [random.uniform(100, 500)],
        'occupancy': [random.choice([0, 1])]
    })
    
    predicted_light_level = model.predict(new_data)
    timestamps.append(hour)
    predictions.append(predicted_light_level[0])

plt.plot(timestamps, predictions)
plt.xlabel('Hour of the Day')
plt.ylabel('Predicted Light Level')
plt.title('Predicted Light Level Over a Day')
plt.show()

