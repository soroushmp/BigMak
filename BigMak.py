import requests
from bs4 import BeautifulSoup

url = input('Enter Target URL: ')
words = []
urls = ['https://' + url, ]
index = 0
while len(urls) != index:
    r = requests.get(urls[index])
    soup = BeautifulSoup(r.content, 'html.parser')
    words += list(set(soup.text.split()))
    for a in soup.find_all('a', href=True):
        link = a['href']
        if 'http' not in link:
            link = urls[0] + link
        if link not in urls and url in link:
            urls.append(link)
            print(link, index)
    index += 1
print('Done!')
print(urls)
print(len(words))
print(words[:50])
