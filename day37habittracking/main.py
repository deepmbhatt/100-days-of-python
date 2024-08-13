import requests
from datetime import datetime

pixela_endpoint = "YOUR PIXELA ENDPOINT"
USERNAME = "YOUR USERNAME"
TOKEN = "YOUR TOKEN"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs" # endpoint for creating a graph
graph_config = {
    "id": "graph2",
    "name": "Cycle Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {     # headers for the request
    "X-USER-TOKEN": TOKEN
}
print(graph_endpoint)

today = datetime.now() # get the current date
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2" # endpoint for creating a pixel
pixel_data = { # data for the pixel
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74"
}

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2/{today.strftime('%Y%m%d')}" # endpoint for updating a pixel
update_data = { # data for the update
    "quantity": "5.5"
}
# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2/{today.strftime('%Y%m%d')}" # endpoint for deleting a pixel
response = requests.delete(url=delete_endpoint, headers=headers) # send a delete request
print(response.text)

