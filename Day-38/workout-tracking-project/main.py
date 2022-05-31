# Day 38 Project - Workout Tracking
import requests
import os

WORKOUT_APP_ID = "cbf58515"
WORKOUT_API_KEY = os.environ(WORKOUT_API_KEY)

request_headers = {
    "x-app-id": WORKOUT_APP_ID,
    "x-app-key": WORKOUT_API_KEY,
    "x-remote-user-id": 0,
}

request_body = {
    
}