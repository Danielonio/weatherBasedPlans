from .client import OpenWeatherMapClient as client

class OpenWeatherMapService:
    def getWeatherFromCoordinates(prompt: str):
        currentWeatherUrl = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'lat': '44.34',
            'lon': '10.99',
        }
        response = client.get(currentWeatherUrl, params)
        print(response)
        return response 


    

