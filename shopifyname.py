import requests
import os
from bs4 import BeautifulSoup
import re

def main2():
	global y
	global x
	a = re.sub('<image:title>', '', str(table))
	a = re.sub('</image:title>', '', a)
	b = re.sub('<loc>', '', str(tablelink))
	b = re.sub('</loc>', '', b)
	print('\n'+a+'\n'+b+'\n')
	x=x+1

def main1():
	global y
	global x
	for word in kw:
		if str(word) in str(table):
			a = re.sub('<image:title>', '', str(table))
			a = re.sub('</image:title>', '', a)
			b = re.sub('<loc>', '', str(tablelink))
			b = re.sub('</loc>', '', b)
			print('\n'+a+'\n'+b+'\n')
			x=x+1
		else:
			y=y+1

def run():
	global kw
	global table
	global soup
	global y
	global x
	global tablelink
	y=0
	x=0
	if link[-1] == '/':
		nlink = link+'sitemap_products_1.xml'
	else:
		nlink = link+'/sitemap_products_1.xml'

	rget = requests.get(nlink).text
	soup = BeautifulSoup(rget, 'lxml')
	tablee = soup.find_all('url')
	for i in tablee:
		tablelink = i.find('loc')
		table = i.find({'image:title'})
		if kw1 == '':
			main2()
		else:
			kw = kw1.split(',')
			main1()
	print('\n\n'+str(x)+' Products Found.')

os.system('clear')
print('Shopify Link Finder by xxxtentabletop#5179\n\nFinds Shopify Links based on name keywords\n')

link = raw_input('Base Link: ')
kw1 = raw_input('Keywords Seperated by a comma (CASE SENSITIVE): ')
run()










