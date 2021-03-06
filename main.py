from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]
#alternative
#for n in range(len(movie_titles) - 1, 0, -1):
    #print(n)

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
