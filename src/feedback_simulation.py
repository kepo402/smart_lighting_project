# feedback_simulation.py
import random
from train_model import model, X_test

def simulate_user_feedback(predicted_level):
    feedback = random.choice(["positive", "negative"])
    print(f"User feedback: {feedback}")
    return feedback

predictions = model.predict(X_test)
for pred in predictions[:5]:
    feedback = simulate_user_feedback(pred)
