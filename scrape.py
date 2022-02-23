"""Scrape module"""
import datetime
import requests
from bs4 import BeautifulSoup


session = requests.Session()


def blic_funct(num):
    """blic web scrape """
    # url
    blic_url = "https://www.blic.rs/search?q=novak+djokovic"

    page = session.get(blic_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all("div", {"class": "content-wrapper"})

    # output dictionary
    blic_dict = {}
    count = 1
    index = 0

    while index < 20:

        # article title
        article_title = data[index].find("p").text
        if "Novak" or "novak" or "NOVAK" in article_title:
            article_dict = {}

            # article date
            article_date = data[index].find("span").text[6:16]
            article_dict["Date"] = article_date

            # adding article title to a dictionary
            article_dict["Title"] = article_title

            # article hyperlink
            article_link = data[index].find(href=True)['href']
            article_dict["Hyperlink"] = article_link

            blic_dict[f'Article number {count}'] = article_dict
            count += 1
            if count > num:
                break
        index += 1
    return blic_dict


def mondo_funct(num):
    """mondo web scrape"""

    # url
    mondo_url = "https://mondo.rs/Novak-Djokovic/tag13798/1"

    page = session.get(mondo_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all("article", {"class": "news-wrapper"})

    # output dictionary
    mondo_dict = {}
    for index in range(num):
        article_dict = {}

        # article date
        article_date_data = data[index].find(
            "p", {"class": "time"}).text.split()
        if "Pre" in article_date_data:
            article_date = datetime.date.today().strftime("%d.%m.%Y")
        else:
            article_date = str(article_date_data[-1])[:-1]
        article_dict["Date"] = article_date

        # article title
        article_title = data[index].find("h2", {"class": "title"}).text
        article_dict["Title"] = article_title

        # article hyperlink
        article_hyperlink = data[index].find(href=True)['href']
        article_dict["Hyperlink"] = article_hyperlink

        mondo_dict[f'Article number {index+1}'] = article_dict
    return mondo_dict
