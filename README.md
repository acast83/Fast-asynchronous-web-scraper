# Fast asynchronous Web Scraper

This script is an asynchronous web scraper that extracts news articles data from two Serbian news websites: [blic.rs](https://www.blic.rs) and [mondo.rs](https://mondo.rs). It is built using
Python's
asyncio library, along with other libraries like BeautifulSoup, httpx, and asyncclick.

## Features

- Asynchronous execution for faster scraping
- Scrapes the latest news articles from blic.rs and mondo.rs
- Customizable search term for scraping relevant articles
- Outputs results in a JSON format

## Requirements

- Python 3.7+
- BeautifulSoup
- httpx
- asyncclick

Install the required libraries with the following command:

```
mkdir scraper
cd sraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

The script can be run from the command line using the following command:

```
python scraper.py -s "srbija danas"
```

### Example Output

The script will output the scraped data in a JSON format like this:

```json
{
  "blic_articles": {
    "article_0": {
      "Date": "26.04.2023",
      "Title": "Some Article Title",
      "Hyperlink": "https://www.blic.rs/some-article-link"
    },
    ...
  },
  "mondo_articles": {
    "article_1": {
      "Date": "26.04.2023",
      "Title": "Another Article Title",
      "Hyperlink": "https://mondo.rs/another-article-link"
    },
    ...
  }
}



