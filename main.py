from bs4 import BeautifulSoup
import requests

web_page = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(web_page,"html.parser")

names = [item.getText() for item in soup.find_all(name = "h3",class_ = "title")]


names.reverse()


with open("Movies Names.txt","w",encoding="utf-8") as file:
    for item in names:
        file.write(item+"\n")

print(names)
