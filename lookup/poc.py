import requests
import json
api_request = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=5BF7FB23-40B5-4BCB-823A-9A64677D9CAB")

api = json.loads(api_request.content)
modified_api = api
for i in range(len(api)):
    if api[i]['Category']['Name'] == "Good":
        modified_api[i]['category_description'] = 'Good air quality.'

    elif api[i]['Category']['Name'] == "Moderate":
        modified_api[i]['category_description'] = 'Moderate air quality.'

    elif api[i]['Category']['Name'] == "Unhealthy for Sensitive Groups":
        modified_api[i]['category_description'] = 'USG air quality.'

    elif api[i]['Category']['Name'] == "Unhealthy":
        modified_api[i]['category_description'] = 'Unhealthy air quality.'

    elif api[i]['Category']['Name'] == "Very Unhealthy":
        modified_api[i]['category_description'] = 'Very  Unhealthy air quality.'

    elif api[i]['Category']['Name'] == "Hazardous":
        modified_api[i]['category_description'] = 'Hazardous air quality.'

print(modified_api)

l  = "Good for"
print(l.lower().replace(" ",""))