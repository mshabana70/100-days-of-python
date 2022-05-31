# Day 38 Project - Workout Tracking
import requests
import os

# APP CONSTANTS
WORKOUT_APP_ID = "cbf58515"
WORKOUT_API_KEY = os.environ(WORKOUT_API_KEY)


# POST Request
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

request_headers = {
    "x-app-id": WORKOUT_APP_ID,
    "x-app-key": WORKOUT_API_KEY,
    "x-remote-user-id": 0,
}

exercise_query = input("How did you exercise today?")
user_gender = input("What is your gender? (male/female)")
user_weight = input("How much do you weigh? (kg)")
user_height = input("How tall are you? (cm)")
user_age = input("How old are you?")

request_body = {
    "query": exercise_query,
    "gender": user_gender,
    "weight_kg": user_weight,
    "height_cm": user_height,
    "age": user_age,
}

exercise_response = requests.post(url=exercise_endpoint, params=request_body, headers=request_headers)
print(exercise_response.raise_for_status())
print(exercise_response.text)