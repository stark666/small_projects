#coding=utf-8
#encode=GB18030
from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv,re


url='http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000'
    #'http://bj.58.com/zufang/?key=%E6%B3%89%E5%B7%9E%E6%88%BF%E5%B1%8B%E5%87%BA%E7%A7%9F&cmcskey=%E6%B3%89%E5%B7%9E%E6%88%BF%E5%B1%8B%E5%87%BA%E7%A7%9F&final=1&jump=1&specialtype=gls'

page=0

csv_file=open('rent.csv','wb')
csv_writer=csv.writer(csv_file,delimiter=',')

while True:
	page+=1
	print 'fetch:',url.format(page=page)
	res=requests.get(url.format(page=page))
	html=BeautifulSoup(res.text,'lxml')
	#print html.encode('GB18030')
	house_list=html.find_all('li')
	#print house_list
	
	if not house_list:
		break

	for house in house_list:
		#print house.encode('GB18030'),'\n'
		try:
			#print house.select('a')[0]['href'],'\n'*4
			house_title=house.select('h2')[0].string.encode('GB18030')
			house_money=house.select('b')[0].string.encode('GB18030')
			house_url=urljoin(url,house.select('a')[0]['href'])
			house_info_list=house_title.split()
			#print type(house_title)
#			print house_title
#			print house_money,house_url,'\n'
			csv_writer.writerow([house_title,house_money,house_url])

		except:
			pass

	
csv_file.close()
