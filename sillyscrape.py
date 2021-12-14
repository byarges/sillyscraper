

from collections import Counter
import collections

import statistics

import requests
import webbrowser
from bs4 import BeautifulSoup

site1="https://www.foxnews.com/"
site2="https://www.nytimes.com/"
site3="https://www.cnn.com/"
site4="https://www.yahoo.com/"
site5="https://www.washingtonpost.com/"



#local vs server toggle
#f = open("index.html", "w")
f = open("/var/www/html/index.html", "w")

def scrapeTheNews(x):
	thislist = []
	filterwords =["New","The","York","Times",
	"in","to", "the","News","for","of","on", "+", "and","a","by","with","is","as","be","after","are","at","or","&","|","from","Is","With","but","has","than","an","your","Do","But","it",">","which","that","have","will","they","That","can","Other","their","how","you","could","my","feedback!","hour","about"]
	the_page = requests.get(x)
	soup = BeautifulSoup(the_page.content, 'html.parser')
	counter=0
	lengthofcounter=0

	for l in filterwords:
		lengthofcounter=lengthofcounter+1

	x=(soup.get_text())
	y=x.split()

	while counter<lengthofcounter:
		for i in y:
			if i == filterwords[counter]:
				y.remove(i)
		counter=counter+1

	clean = Counter(y).most_common(50)
	#htmlfileStart="Top 100 Headline Words of the Hour: </h1>"
	output="<p>"+str(clean)+"</p>"
	return output


def readyToWrite(siteInput):
	stringOutput="<h1>"+str(siteInput)+" top 50 words within this hour</h1>"
	return stringOutput

def combiner(siteForOutput):
	x=readyToWrite(siteForOutput)+scrapeTheNews(siteForOutput)
	return x

f.write(combiner(site1)+combiner(site2)+combiner(site3)+combiner(site4)+combiner(site5))



f.close()