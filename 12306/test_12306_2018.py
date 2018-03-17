#coding=utf-8
#12306售票，api可能经常更换
import requests,re,time,json,prettytable



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

headers={'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'no-cache',
		'Connection':'keep-alive',
		'Cookie':'JSESSIONID=27765F40A1B09FE21F91A441D31D4E15; tk=ip-pJxzLBjBWMha1qmenFikR_ttBDH2ebXuWMEO09AYziY2Y0; _jc_save_detail=true; route=6f50b51faa11b987e576cdb301e545c4; BIGipServerotn=199492106.64545.0000; RAIL_EXPIRATION=1516208795607; RAIL_DEVICEID=MFuik4pYYf-ZlUmBtCK_-t4PtoNKDynvFkfJ-pz6o8c6rmxEWhLzLz94HIVUbGFvIvTcTKfJz_sHjphKpl4Z6IrttCzQuFmJdHGuqJP-_Bo4JjhMnYfnWdyhkjsda4-0xJ2zQyUx8QT4GXx8IVZ7Rc4NmQ6DPbPr; BIGipServerpool_passport=183304714.50215.0000; current_captcha_type=Z; _jc_save_fromStation=%u5357%u4EAC%2CNJH; _jc_save_toStation=%u4E0A%u6D77%2CSHH; _jc_save_fromDate=2018-01-14; _jc_save_toDate=2018-01-14; _jc_save_wfdc_flag=dc',
		'Host':'kyfw.12306.cn',
		'If-Modified-Since':'0',
		'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
		'X-Requested-With':'XMLHttpRequest',
		}



if __name__=='__main__':

	try:
		#print 'local dict'
		station_code_html=open('station_code.txt','r').read().decode('gbk')
		#print '1'
		station_code = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_html)
		station_code_dict = dict(station_code)
		#print 'ok'
	except:
		#print 'net dict'
		station_code_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955"
	                        
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


	#station_code : [('北京东','VAP')，(...)，...]
	#station_code_dict : {'北京东':'VAP'，...:...,}

	#print station_code_dict.get('泉州'.decode('gbk'))

	t=time.strftime("%Y-%m-%d", time.localtime())

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
		query_url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(date,source,to)
	                #https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date= &leftTicketDTO.from_station=  &leftTicketDTO.to_station=  &purpose_codes=ADULT
	                 #https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-06-30&leftTicketDTO.from_station=NKH&leftTicketDTO.to_station=QYS&purpose_codes=ADULT

		requests.packages.urllib3.disable_warnings()
		# query_url='https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-01-14&leftTicketDTO.from_station=NJH&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
  #                 #https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-01-18&leftTicketDTO.from_station=NJH&leftTicketDTO.to_station=QYS&purpose_codes=ADULT
  #                 #https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-01-18&leftTicketDTO.from_station=NJH&leftTicketDTO.to_station=QYS&purpose_codes=ADULT
		ticket_imfor=requests.get(query_url,verify=False)
		# print ticket_imfor.text


		# try:
		rows=ticket_imfor.json().get('data').get('result')
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
			
			price_url='https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=%s&from_station_no=%s&to_station_no=%s&seat_types=OMO&train_date=%s'%(row[2],row[16],row[17],date)
			          #https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=  &from_station_no=  &to_station_no=  &seat_types=OMO&train_date=2018-01-14
			price_url='https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=54000D312520&from_station_no=01&to_station_no=24&seat_types=OMO&train_date=2018-01-18'
			price_imfor=requests.get(price_url,verify=False,headers=headers)
			# print price_url
			print price_imfor.json()
			price_wz=price_imfor.json().get('data').get('WZ')
			price_m=price_imfor.json().get('data').get('M')
			price_A9=price_imfor.json().get('data').get('A9')
			price_0=price_imfor.json().get('data').get('O')

			try:
				price_wz=price_wz.encode('utf-8').split('\xa5')[1]
				price_wz=colored('yellow',price_wz)
			except:
				price_wz='-'
			try:
				price_m=price_m.encode('utf-8').split('\xa5')[1]
				price_m=colored('yellow',price_m)
			except:
				price_m='-'

			try:
				price_A9=price_A9.encode('utf-8').split('\xa5')[1]
				price_A9=colored('yellow',price_A9)
			except:
				price_A9='-'

			try:
				price_0=price_0.encode('utf-8').split('\xa5')[1]
				price_0=colored('yellow',price_0)
			except:
				price_0='-'

			#print price_wz,price_m,price_A9,price_0
			row[6]=station_code_dict.keys()[station_code_dict.values().index(row[6])]
			row[7]=station_code_dict.keys()[station_code_dict.values().index(row[7])]
			row=[row[3], '\n'.join([colored('green', row[6]),  colored('red', row[7])]), '\n'.join([colored('green', row[8]),colored('red', row[9])]), row[10],'\n'.join([row[32],price_A9]), '\n'.join([row[31],price_m]),'\n'.join([row[30],price_0]),row[21], row[23],row[28],row[24],row[29],'\n'.join([row[26],price_wz])]
			#row=[row[3], '\n'.join([colored('green', row[6]),  colored('red', row[7])]), '\n'.join([colored('green', row[8]),colored('red', row[9])]), row[10],row[32], row[31],row[30],row[21], row[23],row[28],row[24],row[29],'\n'.join([row[26],price_wz])]
			trains.add_row(row)
			space=[' ' for i in range(len(row))]
			trains.add_row(space)


		print trains
		# except Exception as e:
		# 	print e
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
