# ---------------------------------------------------------------------
# 
# File          : q_1.py  
# Created       : 09/11/2021 16:14
# Author        : Lukasz S.
# Version       : v1.0.0
# Licencing     : (C) 2021 Lukasz S.
#
# Description   : Scraping website using BeautifulSoup
#
# ---------------------------------------------------------------------

from bs4 import BeautifulSoup
import requests

headings = []


def read_page_contents():
    """ scrape web page contents """

    html_doc = requests.get("http://192.168.178.122")
    soup = BeautifulSoup(html_doc.text, 'html.parser')

    """searching all headings by class : section_headers"""
    for headers in soup.find_all(class_="section_header"):
        headings.append(headers.text.strip())

    print('This are all headings name: {}'.format(headings))

    """count word Apache2"""
    pattern = 'Apache2'
    word = soup.find_all(text=lambda text: text and pattern in text)
    words_count = len(word)

    print("Word Apache2 appears {} times".format(words_count))

    """ find what the title is"""
    title = soup.title

    print("The title of website is: {}".format(title.string))


if __name__ == "__main__":
    read_page_contents()
