import urllib3
from bs4 import BeautifulSoup
import sys, random, re, time


def testIfNextPage(soup):
    next_page = soup.find('a', {'class': 'next_page'})
    if next_page:
        if next_page.has_attr('class') and 'disabled' in next_page['class']:
            return True
        else:
            return False
    else:
        return False


def grabber(base_url, i=1):
    url = "{}?page={}".format(base_url, str(i))
    web = urllib3.PoolManager()
    res = web.request('GET', url)
    soup = BeautifulSoup(res.data, 'html.parser')
    author_divs = soup.find_all(class_='authorOrTitle')
    for div in author_divs:
        div.extract()
    quote_divs = soup.find_all('div', {'class': 'quoteText'})
    allQuotes = []
    for div in quote_divs:
        quote_text = div.get_text()
        allQuotes.append(quote_text)

    editedQuotes = [];
    for quote in allQuotes:
        editedQuotes.append("\n" + quote.strip().strip("“").rstrip("―").strip().strip("”"))

    with open('joyce.txt', 'a') as file:
            print(editedQuotes)
            file.writelines(editedQuotes)
            file.close()

    if i <= 36:
        grabber(base_url, i + 1)

    return


if __name__ == "__main__":
    grabber(''.join(sys.argv[1:]))
