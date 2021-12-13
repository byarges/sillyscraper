

from collections import Counter
import collections

import statistics

import requests
import webbrowser
from bs4 import BeautifulSoup

site1="https://www.foxnews.com/"
site2="https://www.nytimes.com/"

#local vs server toggle
f = open("index.html", "w")
#f = open("/var/www/html/index.html", "w")

def scrapeTheNews(x):
	thislist = []
	filterwords =["New","The","York","Times","in","to", "the","News","for","of","on", "+", "and","a","by","with","is","as","be","after","are","at","or","&","|"]
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

	clean = Counter(y).most_common(100)
	htmlfileStart="Top 100 Headline Words of the Hour: </h1>"
	output=(htmlfileStart+"<p>"+str(clean)+"</p>")
	return output

f.write("<h1> New York Times "+scrapeTheNews(site2)+"</h1>"+"<h1> Fox News "+scrapeTheNews(site1)+"</h1>")
f.close()