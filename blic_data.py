import requests
from bs4 import BeautifulSoup


# url
blic_url = "https://www.blic.rs/search?q=novak+djokovic"

page=requests.get(blic_url)
soup=BeautifulSoup(page.content,'html.parser')
data= soup.find_all("div",{"class":"content-wrapper"})

# output dictionary
blic_dict = {}
n=1
index = 0

while index<20:
    
    # article title
    article_title = data[index].find("p").text
    if "Novak" or "novak" or "NOVAK" in article_title:
        article_dict = {}

        # article date
        article_date = data[index].find("span").text[6:16]
        article_dict["Date"] = article_date

        # adding article title to a dictionary
        article_dict["Title"]=article_title

        # article hyperlink
        article_link =data[index].find(href=True)['href']
        article_dict["Hyperlink"] = article_link

        blic_dict[f'Article number {n}']=article_dict
        n+=1
        if n==6:
            break
    index+=1

print(blic_dict)




