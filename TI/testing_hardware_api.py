import requests

# Set your Steam API key here
API_KEY = "54075376E5294309E88722C73E5C034B"

# Set the Steam ID of the user you want to get friends data for
STEAM_ID = "76561198873808910"

# Set the URL for the Steam API endpoint for getting a user's friends list
URL = "http://api.steampowered.com/ISteamUser/GetFriendList/v1/"

# Set the parameters for the API request
params = {
    "key": API_KEY,
    "steamid": STEAM_ID,
    "relationship": "friend"
}

# Make the API request
response = requests.get(url=URL, params=params)

# Get the user's friends data from the response
friends_data = response.json()["friendslist"]["friends"]

# Print the user's friends data
print(friends_data)

# TODO: Post the user's friends data to a Twitter-like application