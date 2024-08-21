# adjust_lighting.py
from train_model import model, X_test

def adjust_lighting(predicted_level):
    print(f"Adjusting lighting to {predicted_level:.2f} lux.")

predictions = model.predict(X_test)
for pred in predictions[:5]:
    adjust_lighting(pred)
