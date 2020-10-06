from django.shortcuts import render

def welcome(request):
    return render(request, "home.html", {"mesg":"Welcome to AirQualityApp...."})

# Create your views here.
def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']

        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=5BF7FB23-40B5-4BCB-823A-9A64677D9CAB")

        try:
            api = json.loads(api_request.content)
            modified_api = api
            for i in range(len(api)):
                if api[i]['Category']['Name'] == "Good":
                    modified_api[i]['category_description'] = 'Good air quality.'
                    modified_api[i]['category_color'] = api[i]['Category']['Name'].lower().replace(" ", "")

                elif api[i]['Category']['Name'] == "Moderate":
                    modified_api[i]['category_description'] = 'Moderate air quality.'
                    modified_api[i]['category_color'] = api[i]['Category']['Name'].lower().replace(" ", "")

                elif api[i]['Category']['Name'] == "Unhealthy for Sensitive Groups":
                    modified_api[i]['category_description'] = 'USG air quality.'
                    modified_api[i]['category_color'] = 'usg'

                elif api[i]['Category']['Name'] == "Unhealthy":
                    modified_api[i]['category_description'] = 'Unhealthy air quality.'
                    modified_api[i]['category_color'] = api[i]['Category']['Name'].lower().replace(" ", "")

                elif api[i]['Category']['Name'] == "Very Unhealthy":
                    modified_api[i]['category_description'] = 'Very  Unhealthy air quality.'
                    modified_api[i]['category_color'] = api[i]['Category']['Name'].lower().replace(" ", "")

                elif api[i]['Category']['Name'] == "Hazardous":
                    modified_api[i]['category_description'] = 'Hazardous air quality.'
                    modified_api[i]['category_color'] = api[i]['Category']['Name'].lower().replace(" ", "")

        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api, 'modified_api': modified_api})
    return render(request, 'home.html')


def about(request):
    response = "About Me..."
    return render(request, 'about.html', {'res': response})
