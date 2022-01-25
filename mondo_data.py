import requests
from bs4 import BeautifulSoup
import datetime

#url
mondo_url = "https://mondo.rs/Novak-Djokovic/tag13798/1"

page=requests.get(mondo_url)
soup=BeautifulSoup(page.content,'html.parser')
data = soup.find_all("article",{"class":"news-wrapper"})

#output dictionary
mondo_dict = {}
for index in range(5):
    article_dict = {}

    # article date
    article_date_data = data[index].find("p",{"class":"time"}).text.split()
    if "Pre" in article_date_data:
        article_date = datetime.date.today().strftime("%d.%m.%Y")
    else:
        article_date = str(article_date_data[-1])[:-1]
    article_dict["Date"]=article_date

    # article title
    article_title = data[index].find("h2",{"class":"title"}).text
    article_dict["Title"]=article_title

    # article hyperlink
    article_hyperlink = data[index].find(href=True)['href']
    article_dict["Hyperlink"]=article_hyperlink
    
    mondo_dict[f'Article number {index+1}']=article_dict



