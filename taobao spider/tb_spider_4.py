#coding=utf-8
#淘宝数据爬取

import requests,re,json,time,xlwt,random,os
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

	soup = BeautifulSoup(tmp, 'lxml')

	pattern=re.compile(r'"hotCats":(.*?)},"export":false}')
	title = re.findall(pattern, tmp)

	time.sleep(1)

tmp=title[0]

print '*'*120
# print json.loads(tmp)
# for i in json.loads(tmp):
# 	# print i
# 	print i['name'],i['url']
# 	for j in i['subCats']:
# 		print '\t',j['name'],j['url']

workbook = xlwt.Workbook()

for i in json.loads(tmp):
	

	sheet = workbook.add_sheet(i['name'],cell_overwrite_ok=True)
	sheet.write(0,0,u'店铺名')
	sheet.write(0,1,u'宝贝数量')
	sheet.write(0,2,u'总销量')
	sheet.write(0,3,u'店铺网址')
	sheet.write(0,5,u'推荐宝贝')
	# sheet.write(0,4,u'商品名字')
	# sheet.write(0,5,u'商品价格')

	# sheet.write(0,6,u'商品名字')
	# sheet.write(0,7,u'商品价格')

	# sheet.write(0,8,u'商品名字')
	# sheet.write(0,9,u'商品价格')

	# sheet.write(0,10,u'商品名字')
	# sheet.write(0,11,u'商品价格')

	sheet.write(0,4,u'平均价格')


	store_num=500

	# url_02='https://shopsearch.taobao.com'+i['url']+'&isb=1&shop_type=&ratesum=&goodrate='  #&s=20   #&sort=sale-desc
	url_base='https://shopsearch.taobao.com'+i['url']+'&isb=1&shop_type=&ratesum=&goodrate=&s='
	print url_base
	# url_24=url_02+'&s=20'
	# url_46=url_02+'&s=40'
	# url_68=url_02+'&s=60'
	# url_810=url_02+'&s=80'

	all_stores=[]
	# for url in [url_02,url_24,url_46,url_68,url_810]:
	for page in range(0,2000,20):

		print i['name']
		print str(int(float(page)/float(20)))+'%'

		url=url_base+str(page)

		stores=[]
		while stores==[]:

			r=session.get(url)
			tmp=r.text
			soup = BeautifulSoup(tmp, 'lxml')
			pattern=re.compile(r'{"shopItems":(.*?),"apiUrl"')
			stores = re.findall(pattern, tmp)
			time.sleep(1)
		# print type(stores)

		all_stores+=json.loads(stores[0])
		os.system('cls')
	# tmp_stores=all_stores[0]
	# print len(tmp_stores)
	for index,item in enumerate(all_stores):
		try:
			sheet.write(index+1,0,item['rawTitle'])
			sheet.write(index+1,1,item['procnt'])
			sheet.write(index+1,2,item['totalsold'])
			sheet.write(index+1,3,item['shopUrl'])

			# r=session.get(r'http://shop113462750.taobao.com')
			# print r.headers['url-hash']     可得  http://zara.tmall.com/index.htm

			# auc_num=0
			price_mean=0
			for index_auc,auction in enumerate(item['auctionsInshop']):
				# sheet.write(index+1,col_num,auction['title'])
				# col_num+=1
				price_mean+=float(auction['price'])
				pattern_0=u'.*?\u003c/span\u003e\s?([a-zA-Z]*[\u4e00-\u9fa5a-zA-Z0-9]+\(?[\u4e00-\u9fa5a-zA-Z0-9]*\)?).*?'
				pattern_1=u'.*?([a-zA-Z\/]*[\u4e00-\u9fa5a-zA-Z0-9]+\(?[\u4e00-\u9fa5a-zA-Z0-9]*\)?).*?'
				try:
					title=re.match(pattern_0,auction['title']).group(1)
				except:
					title=re.match(pattern_1,auction['title']).group(1)
				sheet.write(index+1,5+index_auc,title)
				# sheet.write(index+1,col_num,auction['price'])
				# col_num+=1
			price_mean/=len(item['auctionsInshop'])
			sheet.write(index+1,4,round(price_mean,1))
			# print j['rawTitle'],j['procnt'],j['totalsold'],j['shopUrl']              #procnt宝贝数量
		except Exception as e:
			print e

	# break

workbook.save('G:\\test.xls')
# workbook.save(os.path.abspath('')+ os.sep + 'tmall_data.xls')
# print u'文件已保存在：',os.path.abspath('')+ os.sep + 'tmall_data.xls'
