import random
import pandas as pd
from datetime import datetime, timedelta
import os

def simulate_sensor_data(days=7):
    data = []
    start_time = datetime.now()
    
    # Generate simulated data
    for day in range(days):
        for hour in range(24):
            time = start_time + timedelta(days=day, hours=hour)
            light_level = random.uniform(100, 500)
            occupancy = random.choice([0, 1])
            data.append({'timestamp': time, 'light_level': light_level, 'occupancy': occupancy})
    
    df = pd.DataFrame(data)

    # Get the absolute path of the project directory
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Construct the absolute path for the CSV file
    data_path = os.path.join(project_dir, 'data', 'simulated_data.csv')

    # Save the DataFrame to the CSV file
    df.to_csv(data_path, index=False)
    print(f"Data simulation complete, saved to {data_path}")

if __name__ == "__main__":
    simulate_sensor_data()
