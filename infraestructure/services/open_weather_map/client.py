import os
import requests
from dotenv import load_dotenv

class OpenWeatherMapClient:
  load_dotenv() 
  apiKey = os.environ.get('OPEN_WEATHER_MAP_API_KEY')

  def get(url:str, params:object):
    params['appid']= OpenWeatherMapClient.apiKey
    postResponse = requests.get(url,  params=params)
    postResponseJson = postResponse.json()
    return postResponseJson