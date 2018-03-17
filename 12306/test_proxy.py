#coding=utf-8
#12306售票，api可能经常更换，使用代理，可能没用
import requests,re,time,json,prettytable,urllib
from bs4 import BeautifulSoup

from test_ip import get_proxy

#print get_proxy()


def colored(color, text):  
	table = {  
		'red': '\033[91m',  
		'green': '\033[92m',
		'yellow':'\033[93m',
		# no color  
		'nc': '\033[0m' 
#	HEADER = '\033[95m'
#    OK_BLUE = '\033[94m'
#    OK_GREEN = '\033[92m'
#    WARING_YELLOW = '\033[93m'
#    FAIL = '\033[36m'
#    FLASHING = '\033[35m'
#    CRITICAL_RED = '\033[31m'
#    END = '\033[0m'
	}  
	cv = table.get(color)  
	nc = table.get('nc')  
	return ''.join([cv, text, nc]) 





try:
	#print 'local dict'
	station_code_html=open(r'.\build\station_code.txt','r').read().decode('gbk')
	#print '1'
	station_code = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_html)
	station_code_dict = dict(station_code)
	#print 'ok'
except Exception,e:
	print e
	#print 'net dict'
	station_code_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955"
        #去除https访问的警告信息
	requests.packages.urllib3.disable_warnings()

#	station_code=urllib.urlopen(station_code_url).read()
	station_code_imfor=urllib.urlopen(station_code_url).read()
	soup=BeautifulSoup(station_code_imfor,'lxml')
	station_code_html=soup.text

#	r = requests.get(station_code_url, verify=False)
#	station_code_html = r.text

	station_code = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_html)
	station_code_dict = dict(station_code)
	f=open(r'.\build\station_code.txt','w')
	#print type(station_code_html)
	f.write(station_code_html.encode('gbk'))
	f.close()


#station_code : [('北京东','VAP')，(...)，...]
#station_code_dict : {'北京东':'VAP'，...:...,}

#print station_code_dict.get('泉州'.decode('gbk'))

#t=time.strftime("%Y-%m-%d", time.localtime())

proxy_temp=None

while True:
	date=raw_input('\n出发日期:'.decode('utf-8').encode('gbk'))
	if not re.match(r'^(20\d{2})\-(0[1-9]|1[0-2])\-([0-2][0-9]|3[0-1])$',date):
		f=re.match(r'^(20\d{2})\ *(0[1-9]|1[0-2])\ *([0-2][0-9]|3[0-1])$',date)
		date='-'.join(f.groups())

	source=station_code_dict.get(raw_input('\n出发地:'.decode('utf-8').encode('gbk')).decode('gbk'))
	to=station_code_dict.get(raw_input('\n目的地:'.decode('utf-8').encode('gbk')).decode('gbk'))
	print ''

	#print source,to

	#query_url = "https://kyfw.12306.cn/otn/leftTicket/log?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT"%(date,source,to)
	#query_url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s'%(date,source,to)
	query_url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(date,source,to)
                 #https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-06-30&leftTicketDTO.from_station=NKH&leftTicketDTO.to_station=QYS&purpose_codes=ADULT

	requests.packages.urllib3.disable_warnings()


	#ticket_imfor=requests.get(query_url,verify=False)
	#print 'proxy:',proxy_temp
	#query_url='http://ip.chinaz.com/getip.aspx'
	ticket_imfor=urllib.urlopen(query_url,proxies=proxy_temp).read()
	#print type(ticket_imfor)
	#print ticket_imfor.decode('utf-8')


	try:
		soup=BeautifulSoup(ticket_imfor,'lxml')
		#print soup.text
		station_dict=json.loads(soup.text)
		rows=station_dict.get('data').get('result')
		#rows=ticket_imfor.json().get('data').get('result')
		#print type(rows)


		trains= prettytable.PrettyTable() 
		row_1=['车次',"车站","时间","历时","商特","一等","二等","高软","软卧","硬卧 ","软座 ","硬座","无座"]
		for i in range(len(row_1)):
			row_1[i]=row_1[i].decode('utf-8')
		trains.field_names=row_1

	#		for index,item in enumerate(rows[0].split('|')):
	#			print index,item
		


		for row in rows :
			#print row
	#	row=row.encode('gbk')
			row=row.split('|')
			for index,item in enumerate(row):
				if item=='':
					row[index]='-'
			
			price_url='https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=%s&from_station_no=%s&to_station_no=%s&seat_types=OM9&train_date=%s'%(row[2],row[16],row[17],date)
			#print price_url
			
			price_imfor= urllib.urlopen(price_url,proxies=proxy_temp).read()
#			print proxy_temp
#			print price_imfor
			soup=BeautifulSoup(price_imfor,'lxml')
			price_imfor_json=json.loads(soup.text)
			#print (price_imfor_json)
			#price_imfor_json=price_imfor.json()
			price_wz=price_imfor_json.get('data').get('WZ')       #无座
			#print type(price_wz),price_wz.encode('GB18030')
			price_m=price_imfor_json.get('data').get('M')         #二等
			price_A9=price_imfor_json.get('data').get('A9')       #商特
			price_0=price_imfor_json.get('data').get('O')         #一等
#			print price_wz,price_m,price_A9,price_0


#			price_wz=price_wz.encode('GB18030').split('??')[0]
#			price_wz=colored('yellow',price_wz)
#			print price_wz
			try:
				price_wz=price_wz.encode('GB18030').split('\x833\xd79')[1]
				#print list(price_wz)
				price_wz=colored('yellow',price_wz)
				#print price_wz
			except:
				price_wz='-'
			try:
				price_m=price_m.encode('GB18030').split('\x833\xd79')[1]
				price_m=colored('yellow',price_m)
			except:
				price_m='-'

			try:
				price_A9=price_A9.encode('GB18030').split('\x833\xd79')[1]
				price_A9=colored('yellow',price_A9)
			except:
				price_A9='-'

			try:
				price_0=price_0.encode('GB18030').split('\x833\xd79')[1]
				price_0=colored('yellow',price_0)
			except:
				price_0='-'

			#print price_wz,price_m,price_A9,price_0
			row[6]=station_code_dict.keys()[station_code_dict.values().index(row[6])]
			row[7]=station_code_dict.keys()[station_code_dict.values().index(row[7])]
			#print 'wz:',price_wz
			row=[row[3], '\n'.join([colored('green', row[6]),  colored('red', row[7])]), '\n'.join([colored('green', row[8]),colored('red', row[9])]), row[10],'\n'.join([row[32],price_A9]), '\n'.join([row[31],price_m]),'\n'.join([row[30],price_0]),row[21], row[23],row[28],row[24],row[29],'\n'.join([row[26],price_wz])]
			#row=[row[3], '\n'.join([colored('green', row[6]),  colored('red', row[7])]), '\n'.join([colored('green', row[8]),colored('red', row[9])]), row[10],row[32], row[31],row[30],row[21], row[23],row[28],row[24],row[29],'\n'.join([row[26],price_wz])]
			trains.add_row(row)
			space=[' ' for i in range(len(row))]
			trains.add_row(space)


		print trains
	except Exception as e:
		print e
		proxy=raw_input('使用代理？(y/n)'.decode('utf-8').encode('gbk'))
		if proxy=='y':
			proxy=get_proxy()
			ip=proxy[0]
			soc=proxy[1]
			proxy_host='http://'+ip+':'+soc
			proxy_temp={'http':proxy_host}

		#print '日期大于售票最大天数,请重试...'.decode('utf-8').encode('gbk')

		#
#	trains= prettytable.PrettyTable() 
#	row_1=['车次',"车站","时间","历时","商特","一等","二等","高软","软卧","硬卧 ","软座 ","硬座","无座"]
#	for i in range(len(row_1)):
#		row_1[i]=row_1[i].decode('utf-8')
#	trains.field_names=row_1
#
#	#test_0=rows[0].split('|')
#	#for index,item in enumerate(test_0):
#	#	print index,item
#	#
#	#test_9=rows[40].split('|')
#	#for index,item in enumerate(test_9):
#	#	print index,item
#	#
#	#test_2=rows[2].split('|')
#	#for index,item in enumerate(test_2):
#	#	print index,item
#	#
#	#test_4=rows[4].split('|')
#	#for index,item in enumerate(test_4):
#	#	print index,item
#
#	#for i in row_1:
#	#	print i,'| ',
#	#print ''
#	 
#	for row in rows :
#	#	row=row.encode('gbk')
#		row=row.split('|')
#		for index,item in enumerate(row):
#			if item=='':
#				row[index]='-'
#			
#	#	print row
#		row[6]=station_code_dict.keys()[station_code_dict.values().index(row[6])]
#		row[7]=station_code_dict.keys()[station_code_dict.values().index(row[7])]
#		row=[row[3], '\n'.join([colored('green', row[6]),  colored('red', row[7])]), '\n'.join([colored('green', row[8]),colored('red', row[9])]), row[10],row[32], row[31],row[30],row[21], row[23],row[28],row[24],row[29],row[26]]
#		trains.add_row(row)
#
#
#	print trains
