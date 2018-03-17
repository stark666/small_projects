#coding=utf-8
#淘宝数据爬取

import requests,re,json,time
from bs4 import BeautifulSoup

session = requests.session()
session.headers = {
'authority':'shopsearch.taobao.com',
'method':'GET',
# 'path':'/search?app=shopsearch&q=&imgfile=&commend=all&ssid=s5-e&search_type=shop&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306',
'scheme':'https',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9',
'cache-control':'max-age=0',
'dnt':'1',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}

title=[]
while title==[]:
	r=session.get('https://shopsearch.taobao.com/search?app=shopsearch&q=&imgfile=&commend=all&ssid=s5-e&search_type=shop&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306')
	tmp=r.text
	# print tmp
	# print tmp==None

	# import re
	soup = BeautifulSoup(tmp, 'lxml')
	# pattern=re.compile(r'{"name":"(.*?)","domClass":".*?","url":"(.*?)","subCats"',re.S)
	pattern=re.compile(r'"hotCats":(.*?)},"export":false}')
	title = re.findall(pattern, tmp)
	# print title
	# print title==[]
	time.sleep(2)
print type(title[0])
tmp=title[0]
# tmp=title[0].encode('GB18030')
# print tmp
print '*'*120
# print json.loads(tmp)
# for i in json.loads(tmp):
# 	# print i
# 	print i['name'],i['url']
# 	for j in i['subCats']:
# 		print '\t',j['name'],j['url']



for i in json.loads(tmp):
	stores=[]
	print i['name']
	while stores==[]:
		url='https://shopsearch.taobao.com'+i['url']+'&isb=1&shop_type=&ratesum=&goodrate=&sort=sale-desc'  #&s=20
		r=session.get(url)
		tmp=r.text
		soup = BeautifulSoup(tmp, 'lxml')
		pattern=re.compile(r'{"shopItems":(.*?),"apiUrl"')
		stores = re.findall(pattern, tmp)
		time.sleep(2)
	tmp_stores=stores[0]
	for j in json.loads(tmp_stores):
		try:
			print j['rawTitle'],j['procnt'],j['totalsold'],j['shopUrl']              #procnt宝贝数量
		except:
			print ''
