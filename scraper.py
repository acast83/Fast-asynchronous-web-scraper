"""Scrape module"""
import asyncio
import datetime
import json
import urllib
from functools import wraps

import asyncclick as click
import httpx
from bs4 import BeautifulSoup


def print_timing(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        print(f"Starting function {func.__name__} at {start}")
        result = await func(*args, **kwargs)  # Add 'await' here
        end = datetime.datetime.now()
        print(f"Ending function {func.__name__} at {end}")

        print(f"Total time elapsed: {end - start}")
        return result

    return wrapper


async def blic_scraper(search_term):
    """blic web scraper function """
    q = urllib.parse.urlencode(
        {'q': search_term})
    # url
    blic_url = f"https://www.blic.rs/search?{q}"

    async with httpx.AsyncClient() as client:
        r = await client.get(blic_url)

    soup = BeautifulSoup(r.text, 'html.parser')

    data = soup.find_all("div", {"class": "news__content"})

    # output dictionary
    blic_dict = {}
    index = 0

    while index < 5:
        # article title
        article_title = data[index].find("a").text

        article_dict = {}

        # article date
        article_date = data[index].find("time").text.strip()
        article_dict["Date"] = article_date

        # adding article title to a dictionary
        article_dict["Title"] = article_title

        # article hyperlink
        article_link = data[index].find(href=True)['href']
        article_dict["Hyperlink"] = article_link

        blic_dict[f'article_{index}'] = article_dict
        index += 1

    return blic_dict


async def mondo_scraper(search_term):
    """mondo web scraper function"""

    q = urllib.parse.urlencode(
        {'q': search_term})
    # url
    mondo_url = f"https://mondo.rs/search/1/1?{q}"

    async with httpx.AsyncClient() as client:

        res = await client.get(mondo_url)

    soup = BeautifulSoup(res.text, 'html.parser')
    data = soup.find_all("article", {"class": "news-wrapper"})

    # output dictionary
    mondo_dict = {}
    for index in range(5):
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

        mondo_dict[f'article_{index + 1}'] = article_dict
    return mondo_dict


@click.command()
@click.option('--search_term', '-s', default="Srbija")
@print_timing
async def web_scraper(search_term: str):
    blic_results, mondo_results = await asyncio.gather(
        blic_scraper(search_term=search_term),
        mondo_scraper(search_term=search_term),
    )

    result = {

        "blic_articles": blic_results,
        "mondo_articles": mondo_results
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(web_scraper())
