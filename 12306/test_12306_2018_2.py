#coding=utf-8
import requests,re,time,json,prettytable
from bs4 import BeautifulSoup
from colored import cs

session = requests.session()

session.headers={'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'no-cache',
		'Connection':'keep-alive',
		# 'Cookie':'JSESSIONID=27765F40A1B09FE21F91A441D31D4E15; tk=ip-pJxzLBjBWMha1qmenFikR_ttBDH2ebXuWMEO09AYziY2Y0; _jc_save_detail=true; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=199492106.64545.0000; RAIL_EXPIRATION=1516208795607; RAIL_DEVICEID=MFuik4pYYf-ZlUmBtCK_-t4PtoNKDynvFkfJ-pz6o8c6rmxEWhLzLz94HIVUbGFvIvTcTKfJz_sHjphKpl4Z6IrttCzQuFmJdHGuqJP-_Bo4JjhMnYfnWdyhkjsda4-0xJ2zQyUx8QT4GXx8IVZ7Rc4NmQ6DPbPr; BIGipServerpool_passport=183304714.50215.0000; current_captcha_type=Z; _jc_save_fromStation=%u5357%u4EAC%2CNJH; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2018-01-14; _jc_save_toDate=2018-01-14; _jc_save_wfdc_flag=dc',
		'Host':'kyfw.12306.cn',
		'If-Modified-Since':'0',
		'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
		'X-Requested-With':'XMLHttpRequest',
		}



try:
	#print 'local dict'
	station_code_html=open('station_code.txt','r').read().decode('gbk')
	#print '1'
	station_code = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_html)
	station_code_dict = dict(station_code)
	#print 'ok'
except:
	#print 'net dict	station_code_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955"
                        
        #去除https访问的警告信息
	requests.packages.urllib3.disable_warnings()
	r = requests.get(station_code_url, verify=False,headers=headers)
	station_code_html = r.text
	station_code = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_html)
	station_code_dict = dict(station_code)
	f=open('station_code.txt','w')
	#print type(station_code_html)
	f.write(station_code_html.encode('gbk'))
	f.close()

t=time.strftime("%Y-%m-%d", time.localtime())

date=raw_input('\n出发日期:'.decode('utf-8').encode('gbk'))
if not re.match(r'^(20\d{2})\-(0[1-9]|1[0-2])\-([0-2][0-9]|3[0-1])$',date):
	f=re.match(r'^(20\d{2})\ *(0[1-9]|1[0-2])\ *([0-2][0-9]|3[0-1])$',date)
	date='-'.join(f.groups())

source=station_code_dict.get(raw_input('\n出发地:'.decode('utf-8').encode('gbk')).decode('gbk'))
to=station_code_dict.get(raw_input('\n目的地:'.decode('utf-8').encode('gbk')).decode('gbk'))

query_url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(date,source,to)
# https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-01-18&leftTicketDTO.from_station=None&leftTicketDTO.to_station=None&purpose_codes=ADULT
# print query_url
while True:
	try:
		r=session.get(query_url)
		ticket_imfor=json.loads(r.content)
		break
	except:
		time.sleep(2)
		pass
rows=ticket_imfor.get('data').get('result')
# print rows

trains= prettytable.PrettyTable() 
row_1=[u'车次',u"车站",u"时间",u"历时",u"商特",u"一等",u"二等",u"高软",u"软卧",u"硬卧 ",u"软座 ",u"硬座",u"无座"]
# for i in range(len(row_1)):
# 	row_1[i]=row_1[i].encode('GB18030')

trains.field_names=row_1

for row in rows :
	row=row.split('|')
	for index,item in enumerate(row):
		if item=='':
			row[index]='-'
	# 	print index,item
	# print '\n','*'*120,'\n'

	price_url='https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=%s&from_station_no=%s&to_station_no=%s&seat_types=OMO&train_date=%s'%(row[2],row[16],row[17],date)
	# price_url='https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=54000D312520&from_station_no=01&to_station_no=24&seat_types=OMO&train_date=2018-01-18'
	print price_url
	
	while True:
		try:
			r=session.get(price_url)
			price_imfor=json.loads(r.content)
			break
		except:
			time.sleep(2)
			pass


	try:
		price_wz=price_imfor.get('data').get('WZ')
		price_wz=price_wz.encode('utf-8').split('\xa5')[1]
	except:
		price_wz='-'

	try:
		price_m=price_imfor.get('data').get('M')
		price_m=price_m.encode('utf-8').split('\xa5')[1]
	except:
		price_m='-'

	try:
		price_A9=price_imfor.get('data').get('A9')
		price_A9=price_A9.encode('utf-8').split('\xa5')[1]
	except:
		price_A9='-'

	try:
		price_0=price_imfor.get('data').get('O')
		price_0=price_0.encode('utf-8').split('\xa5')[1]
	except:
		price_0='-'


	# print price_wz,price_m,price_A9,price_0

	row[6]=station_code_dict.keys()[station_code_dict.values().index(row[6])]
	row[7]=station_code_dict.keys()[station_code_dict.values().index(row[7])]
	row=[row[3], '\n'.join([cs('green', row[6],'bright'),  cs('red', row[7],'bright')]), 
	'\n'.join([cs('green',row[8],'bright'),cs('red', row[9],'bright')]), row[10],
	'\n'.join([row[32],price_A9]), '\n'.join([row[31],price_m]),
	'\n'.join([row[30],price_0]),row[21], row[23],row[28],row[24],row[29],'\n'.join([row[26],price_wz])]

	trains.add_row(row)
	space=[' ' for i in range(len(row))]
	trains.add_row(space)
print trains