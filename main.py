import requests as rq
import datetime as dt
APP_ID = "# You can take it from nutritionix.com"
API_KEY = "You can take it from nutritionix.com"
exercise_header = {
  "x-app-id": APP_ID,
  "x-app-key": API_KEY
}
exercise_text = input("Tell me which exercises you did: ")
parameters = {
  "query": exercise_text,
  "gender": "male",
  "weight_kg": 75,
  "height_cm": 171,
  "age": 22
}
sign_up = rq.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=exercise_header)
sign_up.raise_for_status()
data1 = sign_up.json()
print(data1["exercises"][0]["duration_min"])
now = dt.datetime.now()
workout_data = {
  "workout": {
    "date": now.strftime("%d/%m/%Y"),
    "time": f"{now.hour}:{now.minute}:{now.second}",
    "duration": round(data1["exercises"][0]["duration_min"]),
    "exercise": data1["exercises"][0]["name"].title(),
    "calories": data1["exercises"][0]["nf_calories"]
  }
}
SHEETY_ENDPOINT = "https://api.sheety.co/f1aaf4fe5d6fec8478d22551db5d58c1/myWorkouts/workouts"
SHEETY_AUTH = {
  "Authorization": "You can take it from api.sheety.co"
}
response = rq.post(url=SHEETY_ENDPOINT, headers=SHEETY_AUTH, json=workout_data)
response.raise_for_status()
