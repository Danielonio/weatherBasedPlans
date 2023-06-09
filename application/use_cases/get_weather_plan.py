from infraestructure.services.open_ai.service import OpenAiService as aiService
from infraestructure.services.open_weather_map.service import OpenWeatherMapService as weatherService
from domain.weather_plan_prompt import weatherPromptTemplate
from datetime import date

class GetWeatherPlan:
    def call(lat, long):
        weatherInfo = weatherService.getWeatherFromCoordinates(lat, long)
        print(weatherInfo)
        recommendationPrompt = weatherPromptTemplate.substitute(
           todayDate= date.today(),
           weatherDescription= weatherInfo['weatherDescription'],
           coordinates= weatherInfo['coordinates'],
           temperature= weatherInfo['temperature'],
        )
        return aiService.getChatGptChatCompletion(recommendationPrompt)

