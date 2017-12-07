import urllib2
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest


URL="https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids/?utm_term=.ee8b2a80ed71"
    # "https://www.washingtonpost.com/news/on-leadership/wp/2017/11/20/episode-11-of-the-constitutional-podcast-war/?hpid=hp_hp-more-top-stories-2_constitutional-930am%3Ahomepage%2Fstory&utm_term=.a97208dd82be"
page= urllib2.urlopen(URL).read().decode('utf-8','ignore')
soup= BeautifulSoup(page,"lxml")
text= soup.find('article').text
text=text.encode('ascii', errors='replace').replace("?"," ")

sentences= sent_tokenize(text)
# print sentences

words=word_tokenize(text.lower())
stopwordsAndPunctuation= set(stopwords.words('english') + list(punctuation))
words= [word for word in words if word not in stopwordsAndPunctuation]
# print words

freq=FreqDist(words)
# print freq
# print nlargest(11,freq,freq.get)

from collections import defaultdict
ranking =defaultdict(int)

for i, sent in enumerate(sentences):
    for w in word_tokenize(sent.lower()):
        if w in freq:
            ranking[i]+=freq[w]

rankedSentences=nlargest(3,ranking,ranking.get)
print rankedSentences

print [sentences[j] for j in sorted(rankedSentences)]