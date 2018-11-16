import requests
import json

# INSERT YOUR LUIS ENDPOINT URL HERE *it's example URL*
API_ENDPOINT = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/4559e6f0-c1d2-4e3c-a1c4-630472097533?subscription-key=16b85f73be424d1b9337dba9dcb18fe5&timezoneOffset=-360&q="

def get_command(command):
	r = requests.get(API_ENDPOINT + command)
	data = json.loads(r.text)
	return data['topScoringIntent']['intent']
