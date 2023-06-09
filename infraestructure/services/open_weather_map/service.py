from .client import OpenWeatherMapClient as client

class OpenWeatherMapService:
    def getWeatherFromCoordinates(lat,long):
        currentWeatherUrl = 'https://api.openweathermap.org/data/2.5/weather'
        params = {
            'lat': lat,
            'lon': long,
        }
        response = client.get(currentWeatherUrl, params)

        adaptedInfo = {
            'coordinates': response['coord'],
            'weatherDescription': response['weather'][0]['description'],
            'temperature': response['main']['temp'],
        }
        return adaptedInfo


    

