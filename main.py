
import requests
# swapi, has all character info - btw this takes f*ckin forever to call
# Creating a class for the API to be called by main later.


class StarWarzApi:
    url = "https://swapi.dev/api/people/"

    # store the starwars api data
    # note - Ryan the def __init__(self) is basically a consturctor in c# . Can change the self part to whatever.
    def __init__(self):
        self.all_people_data = []
        self.search_results = []

    # Call a instance of the sw url  . Def is a function
    def get_people(self):
        url = self.url
        while url:
            response = requests.get(url)

            # check if good response from api
            if response.status_code == 200:
                # create as json objs
                data = response.json()
                # get the newly constructed array and add the api results
                # 'results '- means if it exists ... the 200 status code also confirms
                self.all_people_data.extend(data.get('results', []))
                url = data.get('next')
                # just a check
            else:
                print(
                    f"Failed to retrieve data. Status code: {response.status_code}")
                break

    # Search function - uses the search results array from the constructor. And parses search term as an arg
    def search_people(self, search_term):
        self.search_results = [
            person for person in self.all_people_data if search_term.lower() in person['name'].lower()]

# Dispalys search results, but uses the search results array instead of all the star wars people
    def display_search_results(self):
        for person in self.search_results:
            print("Name: ", person['name'])
            print("Height: ", person['height'])
            print("Mass: ", person['mass'])
            print("Hair Color: ", person['hair_color'])


# This intiates and acts as the main method. The first entry point for the program
if __name__ == "__main__":

    star_wars_api = StarWarzApi()
    star_wars_api.get_people()

    search_term = input("Enter a name to search for: ")
    star_wars_api.search_people(search_term)
    star_wars_api.display_search_results()
