# Smart Lighting Automation Project

## Overview

This project simulates a smart lighting system using machine learning to predict optimal lighting levels based on simulated sensor data. The system generates data, trains a predictive model, evaluates its performance, and visualizes predictions to understand how lighting conditions change throughout the day.

## Components

1. **Data Simulation**
   - Generates simulated sensor data for light levels, occupancy, temperature, and humidity.

2. **Model Training**
   - Trains a RandomForestRegressor model to predict preferred light levels based on the simulated data.

3. **Model Evaluation**
   - Evaluates the model's performance using metrics such as Mean Absolute Error (MAE) and R^2 Score.

4. **Visualization**
   - Uses Matplotlib to plot predicted light levels over different hours of the day.


## Installation

1. **Clone the Repository:**
   git clone https://github.com/kepo402/smart_lighting_project.git
   cd smart_lighting_project
   pip install -r requirements.txt
   
## Create a requirements.txt file with the following content:
pandas
scikit-learn
matplotlib

## Usage
Generate Simulated Data:

Run the script to generate simulated sensor data.

python src/simulate_data.py

Train the Model:

Train the RandomForestRegressor model using the simulated data.

python src/train_model.py
Visualize Predictions:

## Run the script to visualize the model’s predictions for different times of the day.

python src/visualize_predictions.py

Files
**src/simulate_data.py:** Script to generate simulated sensor data and save it as a CSV file.
**src/train_model.py:** Script to train the model and evaluate its performance.
**src/visualize_predictions.py:** Script to visualize the model’s predictions over time.

## Contributing
Feel free to fork the repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.


## Contact
If you have any questions or suggestions, feel free to contact me at alawodeolayinka2@gmail.com.
