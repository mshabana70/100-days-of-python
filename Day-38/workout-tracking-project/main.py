# Day 38 Project - Workout Tracking
# spreadsheet-link: https://docs.google.com/spreadsheets/d/1Bz2VNCPgmUXHiBh62bZ7IxzdZARBNFYtrTBGu_u2b-8/edit#gid=0

import requests
import os
from datetime import datetime

# APP CONSTANTS
WORKOUT_APP_ID = os.environ.get("WORKOUT_APP_ID")
WORKOUT_API_KEY = os.environ.get("WORKOUT_API_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")


# Exercise POST Request
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

request_headers = {
    "x-app-id": WORKOUT_APP_ID,
    "x-app-key": WORKOUT_API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json",
}

# User input
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

# Grab returned response
exercise_data = exercise_response.json()["exercises"]

# Get current date and time
current = datetime.now()
current_date = current.strftime("%d/%m/%Y")
current_time = current.strftime("%H:%M:%S")
# print(current_date)
# print(current_time)

# Sheety POST Request

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

# for every exercise:
for exercise in exercise_data:

    # Format data for spreadsheet
    exercise_name = exercise["name"].title()
    exercise_duration = exercise["duration_min"]
    exercise_calories = exercise["nf_calories"]

    # set request for sheety with exercise and datetime data
    #print(f"Name: {exercise_name}, duration: {exercise_duration}, calories burned: {exercise_calories}")

    sheety_body = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": exercise_calories,
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_body, headers=sheety_headers)
    print(sheety_response.raise_for_status())
    


