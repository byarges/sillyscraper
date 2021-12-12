

from collections import Counter
import collections

import statistics

import requests
import webbrowser
from bs4 import BeautifulSoup

thislist = []
filterwords =["in","to", "the","News","for","of","on"]
the_page = requests.get("https://www.foxnews.com/")
soup = BeautifulSoup(the_page.content, 'html.parser')
f = open("demofile.html", "w")
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


print(Counter(y).most_common(100))

f.write(str(clean))


f.close()
