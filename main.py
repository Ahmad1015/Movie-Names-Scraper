from bs4 import BeautifulSoup
import requests

web_page = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text
soup = BeautifulSoup(web_page,"html.parser")

names = [item.getText() for item in soup.find_all(name = "h3",class_ = "title")]
release_date = [int(item.getText()) for item in soup.find_all(name = "strong")]

print(release_date)
print(names)