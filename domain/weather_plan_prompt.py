from string import Template


weatherPromptTemplate: Template = Template(
'''
Today is $todayDate
Currently I find myself in  the following coordinates: $coordinates , 
the weather could be defined as "$weatherDescription"
and the temperature is $temperature. 


Taking into account the time and weather info I just gave you, recommend
three interesting cultural activities near my location coordinates. For your answer I expect that you are aware of 
the time, place and weather i just gave you. For example, if it's raining, do not recommend outdoors 
activities. Include in your answer the reaseon why you picked those activites in relation to the weather.

Your answer must be an array in JSON format like so:
[{
 activityName: a,
 locationAddress: b,
 reasonBasedOnWeather: c,
 stimatePriceInEuros: d
}]
'''
)
