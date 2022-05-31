# Day 38 Project - Workout Tracking
import requests
import os

# APP CONSTANTS
WORKOUT_APP_ID = os.environ.get("WORKOUT_APP_ID")
WORKOUT_API_KEY = os.environ.get("WORKOUT_API_KEY")


# POST Request
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

request_headers = {
    "x-app-id": WORKOUT_APP_ID,
    "x-app-key": WORKOUT_API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}

exercise_query = str(input("How did you exercise today?"))
user_gender = str(input("What is your gender? (male/female)"))
user_weight = float(input("How much do you weigh? (kg)"))
user_height = float(input("How tall are you? (cm)"))
user_age = int(input("How old are you?"))

request_body = {
    "query": exercise_query,
    "gender": user_gender,
    "weight_kg": user_weight,
    "height_cm": user_height,
    "age": user_age,
}

# request body must be in json format
exercise_response = requests.post(url=exercise_endpoint, json=request_body, headers=request_headers)
print(exercise_response.raise_for_status())
print(exercise_response.text)