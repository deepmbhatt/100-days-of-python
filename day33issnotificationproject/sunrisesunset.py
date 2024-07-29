import requests
parameters = {
    "lat":23.014509,
    "lng":72.591759,
    "formatted":0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params = parameters)


if response.status_code != 200:
    raise Exception("Failed to get the data")
else:
    print("Success")
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1].split("+")[0])
print(sunset.split("T")[1].split("+")[0])
