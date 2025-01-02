"""
Project: Web Scraping Quotes

Task: Scraping quotes and authors from 'quotes.toscrape.com'
Tech: Python, requests, BeautifulSoup, pandas
Author: Sunny Sul. (github.com/sunnysul)
A web scraping script to extract quotes and their authors from 'quotes.toscrape.com'.
The script uses requests for HTTP requests, BeautifulSoup for HTML parsing,
and pandas for data manipulation and CSV export.
Functions:
    get_quotes(url: str, pagesNum: int) -> list:
        Scrapes quotes and authors from multiple pages of the website.
        Args:
            url (str): The base URL of the website to scrape
            pagesNum (int): Number of pages to scrape
        Returns:
            list: A list of dictionaries containing quotes and their authors
                  Each dictionary has 'quote' and 'author' as keys
Global Variables:
    base_url (str): The base URL of the website
    Quotes (list): Storage for scraped quotes and authors
Output:
    Creates a CSV file named 'Quotes.csv' containing all scraped quotes and authors
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://quotes.toscrape.com/"
Quotes = []

# Test Syntax and functonality To Clearify the process

# url = "/page/1"
# res = requests.get(base_url + url)
# soup = BeautifulSoup(res.text, "html.parser")
# quote->span>.text
# quote>span>small>.author
# print(soup.prettify())
# qutes = soup.find_all("span", class_="text")
# authors = soup.find_all("small", class_="author")

# for i in range(len(qutes)):
#     print(qutes[i].text)
#     print(authors[i].text)
#     print()


# Final Function

def get_quotes(url, pagesNum):
    for i in range(pagesNum):
        res = requests.get(url + f"/page/{i+1}")
        soup = BeautifulSoup(res.text, "html.parser")
        qutes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")
        for i in range(len(qutes)):
            Quotes.append({"quote": qutes[i].text, "author": authors[i].text})
    return Quotes


Quotes = get_quotes(base_url, 10)
df = pd.DataFrame(Quotes)
df.to_csv("Quotes.csv", index=False)
