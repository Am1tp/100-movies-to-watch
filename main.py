import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

with open(file="movies_list.txt", mode="w", encoding="utf-8") as file:

    website = requests.get(url=URL).text
    soup = BeautifulSoup(website, "html.parser")
    titles = [title.getText() for title in soup.find_all("h3", class_="title")][::-1]  # reversed list

    for title in titles:
        file.write(title + "\n")



