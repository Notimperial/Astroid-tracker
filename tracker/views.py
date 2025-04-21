from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
api_key = os.getenv("NASA_API_KEY")

# Create your views here.
def home(request):
    START_DATE = "2025-04-13"
    END_DATE = "2025-04-19"



    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={START_DATE}&end_date={END_DATE}&api_key={api_key}"

    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")


    if response.status_code == 200:
        data = response.json()

        astroids = data.get("near_earth_objects")
        
        

        asteroid_details = {}
        for date, asteroids_list in astroids.items():
            asteroid_details[date] = []
            for asteroid in asteroids_list:
                # Collecting relevant data for each asteroid
                asteroid_info = {
                    'name': asteroid.get('name'),
                    'size_min': asteroid['estimated_diameter']['kilometers']['estimated_diameter_min'],
                    'size_max': asteroid['estimated_diameter']['kilometers']['estimated_diameter_max'],
                    'velocity_kmps': asteroid['close_approach_data'][0]['relative_velocity']['kilometers_per_second'],
                    'miss_distance_km': asteroid['close_approach_data'][0]['miss_distance']['kilometers'],
                }
                asteroid_details[date].append(asteroid_info)

        return render(request, "home.html", {"asteroids": asteroid_details})

    
    else:
        return HttpResponse("Error fetching data from NASA API")



# for Heatmap
def heatmap(request):
    return HttpResponse("This is the heatmap page.")
