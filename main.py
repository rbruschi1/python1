
import requests
api_url = "https://swapi.dev/api/people/1"
response = requests.get(api_url)
response.json()
print(response)
print(response.json())