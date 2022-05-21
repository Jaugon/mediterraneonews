import requests
from bs4 import BeautifulSoup

url = str(input("Introduce link de la noticia: "))

result = requests.get(url)
src = result.content
soup = BeautifulSoup(src,"html.parser")
for i in soup.find_all('p', {'class': 'article-body__text'}):
    print(i.get_text().replace("\n"," "))
