import urllib2
from bs4 import BeautifulSoup

url ='https://www.washingtonpost.com'
page= urllib2.urlopen(url).read().decode('utf-8','ignore')
soup= BeautifulSoup(page,"lxml")
# text= soup.find('article').text
text= ' '.join(map(lambda p:p.text, soup.find_all('article')))
print text