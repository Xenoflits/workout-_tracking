import requests
from datetime import datetime



APP_ID = "2441c7fd"
APP_KEY = "2f7caaa9208f72b208aee489a8290f7a"


headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

query = input("please enter your workout \n")

options = {
    "query": query,

}
url="https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url, json=options, headers=headers)

workout_data = response.json()
print(workout_data['exercises'][0])

# sheety
GET_URL = "https://api.sheety.co/10e553c4ee309d0c285c7bdac0321e2b/workouts/workouts"
POST_URL = "https://api.sheety.co/10e553c4ee309d0c285c7bdac0321e2b/workouts/workouts"
date = datetime.now()
formatted_date = date.strftime("%d/%m/%Y")
formatted_time = date.strftime("%H:%M:%S")


data = {
    "workout":{
        "date": formatted_date,
        "time": formatted_time,
        "exercise": workout_data['exercises'][0]['name'],
        "duration": workout_data['exercises'][0]['duration_min'],
        "calories": workout_data['exercises'][0]['nf_calories']
    }
}

result = requests.post(POST_URL,json=data)

print(result.text)

result = requests.get(GET_URL)

print(result.text)
