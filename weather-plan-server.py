from flask import Flask, request
from infraestructure.services.open_ai.service import OpenAiService as aiService
from application.use_cases.get_weather_plan import GetWeatherPlan 

app = Flask(__name__)
@app.route('/', methods=['GET'])
def search():
    args = request.args
    return GetWeatherPlan.call(args['lat'],args['long'])


app.run(host='0.0.0.0', port=81)