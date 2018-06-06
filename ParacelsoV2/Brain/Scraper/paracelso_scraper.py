from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://www.google.com.br')
bsObj = BeautifulSoup(html.read(), 'lxml')
print(bsObj.html.body.div)
