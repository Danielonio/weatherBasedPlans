from infraestructure.services.open_ai.service import OpenAiService as aiService
from infraestructure.services.open_weather_map.service import OpenWeatherMapService as weatherService
from domain.weather_plan_prompt import weatherPromptTemplate
from datetime import date

class GetWeatherPlan:
    def call(characterName):
        weatherService.getWeatherFromCoordinates('hh')
        recommendationPrompt = weatherPromptTemplate.substitute(
           todayDate= date.today(),
           weatherDescription= 'Super sunny day',
           coordinates= "'lat': '44.34', 'lon': '10.99'",
           temperature= '294'
        )
        return aiService.getChatGptChatCompletion(recommendationPrompt)

