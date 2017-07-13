from bs4 import BeautifulSoup
import requests

query = "battery"
query = query.replace(' ', '+')

searchlist = ["https://www.honeywell.com/", "http://www.emerson.com/en-us" ,
			  "https://www.ge.com/","https://www.yokogawa.com/in/",
			  "http://www.alstom.com/india/","http://www.mitsubishi-motors.com/",
			  "http://www.hitachi.co.in/","https://www.toshiba-india.com/",
			  "http://www.schneider-electric.co.in/en/","http://new.abb.com"]

for website in searchlist:
	address = "https://www.google.com/search?q=site:" + website + "+" + query

#headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
	r  = requests.get(address)
	data = r.text
	soup = BeautifulSoup(data, 'html.parser')
	links = []
	print website
	i = 0
	for x in soup.findAll("div", class_= "kv" ):
		links.append(x.cite.text)
		if(i<3):
			print x.cite.text
			i+=1
	