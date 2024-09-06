import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
website_html = response.text 

soup = BeautifulSoup(website_html, "html.parser")   # Parse the HTML content of the website
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")    # Find all the movies in the website
movie_titles = [movie.getText() for movie in all_movies]    # Get the text of the movie titles
movies = movie_titles[::-1]   # Reverse the list of movies
print(movies)   

with open("day45100Moviestowatch/movies.txt", mode="w") as file:    # Write the movies to a file
    for movie in movies:    # Write each movie to the file
        file.write(f"{movie}\n")

