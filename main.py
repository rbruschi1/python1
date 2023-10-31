
import requests
# swapi, has all character info
url = "https://swapi.dev/api/people/"
# response = requests.get(api_url)
# jsonwebdata = response.json()
# print(response)
# print(response.json())

# store the starwars api data
character_data = []

while url:
    # Send an HTTP GET request to the API
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Append the results (people) to the all_people_data list
        character_data.extend(data.get('results', []))

        # Check if there's a next page
        url = data.get('next')
    else:
        # If the request was not successful, print an error message
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        break

# Now, all_people_data contains data for all people
for person in character_data:
    print("Name: ", person['name'])
    print("Height: ", person['height'])
    print("Mass: ", person['mass'])
    print("Hair Color: ", person['hair_color'])
