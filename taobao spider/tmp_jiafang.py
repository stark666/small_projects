#coding=utf-8

import requests,re,json,time,xlwt,random,os
from bs4 import BeautifulSoup


def jiafang(page=0):
	url='https://shopsearch.taobao.com/search?app=shopsearch&ie=utf8&initiative_id=staobaoz_20180117&js=1&q=%E5%AE%B6%E7%BA%BA&suggest=0_1&_input_charset=utf-8&wq=jiafang&suggest_query=jiafang&source=suggest&isb=1&shop_type=&ratesum=&goodrate=&s='
	workbook = xlwt.Workbook()
	session = requests.session()
	requests.packages.urllib3.disable_warnings()
	all_stores=[]




	session.headers = {
			'authority':'shopsearch.taobao.com',
			'method':'GET',
			# 'path':'/search?app=shopsearch&ie=utf8&initiative_id=staobaoz_20180117&js=1&q=%E5%AE%B6%E7%BA%BA&suggest=0_1&_input_charset=utf-8&wq=jiafang&suggest_query=jiafang&source=suggest&isb=1&shop_type=&ratesum=&goodrate=&s='+str(page),
			'scheme':'https',
			'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'accept-encoding':'gzip, deflate, br',
			'accept-language':'zh-CN,zh;q=0.9',
			'cache-control':'max-age=0',
			'connection':'keep-alive',
			'dnt':'1',
			'upgrade-insecure-requests':'1',
			'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
			}
	# for page in range(40,1360,20):
	stores=[]
	# print str(int(float(page)/float(20)))+'%'
	url+=str(page)
	while stores==[]:
		print u'请等待...'
		r=session.get(url,verify=False)
		tmp=r.text
		soup = BeautifulSoup(tmp, 'lxml')
		pattern=re.compile(r'{"shopItems":(.*?),"apiUrl"')
		stores = re.findall(pattern, tmp)
		time.sleep(random.uniform(2,5))
	return json.loads(stores[0])
	# print type(stores)

	# stores=json.loads(stores[0])
	# os.system('cls')
def to_sheet(all_stores):
	workbook = xlwt.Workbook()
	sheet = workbook.add_sheet(u'家纺',cell_overwrite_ok=True)
	sheet.write(0,0,u'店铺名')
	sheet.write(0,1,u'宝贝数量')
	sheet.write(0,2,u'总销量')
	sheet.write(0,3,u'店铺网址')
	sheet.write(0,4,u'平均价格')
	sheet.write(0,5,u'推荐宝贝')

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
				pattern=u'[\u4e00-\u9fa5\(\)a-zA-Z0-9]+'
				title=re.findall(pattern,auction['title'])
				sheet.write(index+1,5+index_auc,title)
				# sheet.write(index+1,col_num,auction['price'])
				# col_num+=1
			price_mean/=len(item['auctionsInshop'])
			sheet.write(index+1,4,round(price_mean,1))
			# print j['rawTitle'],j['procnt'],j['totalsold'],j['shopUrl']              #procnt宝贝数量
			index+=1
		except Exception as e:
			print e

	workbook.save(r'G:\jiafang\test_jiafang.xls')


if __name__=='__main__':
	all_stores=[]
	for page in range(0,1340,20):
		print page
		stores=jiafang(page)
		all_stores+=stores
	to_sheet(all_stores)