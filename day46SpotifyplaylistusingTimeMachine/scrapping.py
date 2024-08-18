import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(url)

website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

all_songs = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in all_songs]
print(song_names)