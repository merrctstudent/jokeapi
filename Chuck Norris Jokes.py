import requests
import json

url = "https://api.icndb.com/jokes/random"

payload={}
headers = {
  'Accept' : 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

jokeJSON = response.json()

print("Here is your official Chuck Norris Joke! " + str(jokeJSON["value"]["joke"]))
