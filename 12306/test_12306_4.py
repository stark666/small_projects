#coding=utf-8
import requests,json,time,re,prettytable
from PIL import Image  
from random import randint
from urllib import unquote
from colored import cs

requests.packages.urllib3.disable_warnings()

class login12306():
	def __init__(self):
		self.headers={'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'no-cache',
		'Connection':'keep-alive',
		'Host':'kyfw.12306.cn',
		'If-Modified-Since':'0',
		'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
		'X-Requested-With':'XMLHttpRequest',
		}
		self.session=requests.session() 

	def get_captcha(self):
		captcha_url='https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.9669841319527472'
		response =self.session.get(url=captcha_url,headers=self.headers,verify=False)
		with open('captcha.jpg','wb') as f:  
			f.write(response.content)  
		im=Image.open('captcha.jpg')
		im.show()
		im.close()
		answer=raw_input('符合的问题的答案是: '.decode('utf-8').encode('gbk'))
		answer_index=filter(lambda x:x not in [' ',','],list(answer))
		# print answer_index
		ans_loc=[[40,40],[115,40],[190,40],[260,40],[40,120],[115,120],[190,120],[260,120]]
		ans_loc=[[x[0]+randint(-10,10),x[1]+randint(-10,10)] for x in ans_loc]

		answer=[]
		for i in answer_index:
			answer+=ans_loc[int(i)-1]
		answer=[str(i) for i in answer]
		return ','.join(answer)

		# --------------------------------------
		#         |         |         |  
		#    1    |    2    |    3    |     4  
		#  40,40  | 115,40  | 190,40  |  260,40 
		# ---------------------------------------  
		#         |         |         |  
		#    5    |    6    |    7    |     8  
		#  40,120 | 115,120 | 190,120 |  260,120
		# ---------------------------------------  

	def check_captcha(self):
		ans_loc=self.get_captcha()
		check_url='https://kyfw.12306.cn/passport/captcha/captcha-check'
		post_data={
					'answer':ans_loc,
					'login_site':'E',
					'rand':'sjrand'
		}
		r=self.session.post(url=check_url,data=post_data,headers=self.headers)
		# print r.content.decode('utf-8').encode('gbk')
		code=json.loads(r.content)['result_code']
		print json.loads(r.content)['result_message']
		if code=='4':
			return True
		#{"result_message":"验证码校验成功","result_code":"4"}

	def login(self):
		# username=raw_input('用户名 :'.decode('utf-8').encode('gbk'))
		# password=raw_input('密码 :'.decode('utf-8').encode('gbk'))
		login_url='https://kyfw.12306.cn/passport/web/login'
		headers_1={
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate, sdch',
			'Accept-Language':'zh-CN,zh;q=0.8',
			'Connection':'keep-alive',
			'Host':'kyfw.12306.cn',
			'Referer':'https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
				}
		headers_2={
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate',
			'Accept-Language':'zh-CN,zh;q=0.8',
			'Cache-Control':'max-age=0',
			'Connection':'keep-alive',
			# 'Content-Length':'10',
			'Content-Type':'application/x-www-form-urlencoded',
			'Host':'kyfw.12306.cn',
			'Origin':'https://kyfw.12306.cn',
			'Referer':'https://kyfw.12306.cn/otn/login/init',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
				}
		headers_4={
			'Accept':'application/json, text/javascript, */*; q=0.01',
			'Accept-Encoding':'gzip, deflate',
			'Accept-Language':'zh-CN,zh;q=0.8',
			'Connection':'keep-alive',
			'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
			'Host':'kyfw.12306.cn',
			'Origin':'https://kyfw.12306.cn',
			'Referer':'https://kyfw.12306.cn/otn/login/init',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
			'X-Requested-With':'XMLHttpRequest',
			}
		data={
				'username':'Young666666',
				'password':'**********',
				'appid':'otn'
		}
		# self.session.get(url='https://kyfw.12306.cn/otn/login/userLogin',headers=headers_1)
		# self.session.post(url='https://kyfw.12306.cn/otn/login/userLogin',headers=headers_2,data={'_json_att':''})
		# self.session.get(url='https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin',headers=headers_2)
		result=self.session.post(url=login_url,data=data,headers=headers_4)
		# print result.content.decode('utf-8').encode('GB18030')
		try:
			result=json.loads(result.content)
			print '\n',result['result_message']
			if result['result_code']==0:
				return True
		except:
			print u'请等待...'

	def left_ticket_imfor(self):
		headers={'Accept':'*/*',
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
			station_code_html=open('station_code.txt','r').read().decode('gbk')
			station_code = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_html)
			station_code_dict = dict(station_code)
		except:
			requests.packages.urllib3.disable_warnings()
			r = requests.get(station_code_url, verify=False,headers=headers)
			station_code_html = r.text
			station_code = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_html)
			station_code_dict = dict(station_code)
			f=open('station_code.txt','w')
			#print type(station_code_html)
			f.write(station_code_html.encode('gbk'))
			f.close()

		date=raw_input('\n出发日期:'.decode('utf-8').encode('gbk'))
		if not re.match(r'^(20\d{2})\-(0[1-9]|1[0-2])\-([0-2][0-9]|3[0-1])$',date):
			f=re.match(r'^(20\d{2})\ *(0[1-9]|1[0-2])\ *([0-2][0-9]|3[0-1])$',date)
			date='-'.join(f.groups())
		source_cn=raw_input('\n出发地:'.decode('utf-8').encode('gbk'))
		to_cn=raw_input('\n目的地:'.decode('utf-8').encode('gbk'))

		source=station_code_dict.get((source_cn).decode('gbk'))
		to=station_code_dict.get((to_cn).decode('gbk'))

		query_url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(date,source,to)
		while True:
			try:
				r=self.session.get(query_url,headers=headers)
				ticket_imfor=json.loads(r.content)
				break
			except:
				time.sleep(1)
				pass
		rows=ticket_imfor.get('data').get('result')
		trains= prettytable.PrettyTable() 
		row_1=[u'车次',u"车站",u"时间",u"历时",u"商特",u"一等",u"二等",u"高软",u"软卧",u"硬卧 ",u"软座 ",u"硬座",u"无座"]
		trains.field_names=row_1
		for row in rows :
			row=row.split('|')
			for index,item in enumerate(row):
				if item=='':
					row[index]='-'
			price_url='https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=%s&from_station_no=%s&to_station_no=%s&seat_types=OMO&train_date=%s'%(row[2],row[16],row[17],date)

			while True:
				try:
					r=self.session.get(price_url,headers=headers)
					price_imfor=json.loads(r.content)
					break
				except:
					time.sleep(1)
					pass
			print price_url
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

			row[6]=station_code_dict.keys()[station_code_dict.values().index(row[6])]
			row[7]=station_code_dict.keys()[station_code_dict.values().index(row[7])]
			row=[row[3], '\n'.join([cs('green', row[6],'bright'),  cs('red', row[7],'bright')]), 
			'\n'.join([cs('green',row[8],'bright'),cs('red', row[9],'bright')]), row[10],
			'\n'.join([row[32],price_A9]), '\n'.join([row[31],price_m]),
			'\n'.join([row[30],price_0]),row[21], row[23],row[28],row[24],row[29],'\n'.join([row[26],price_wz])]

			trains.add_row(row)
			space=[' ' for i in range(len(row))]
			trains.add_row(space)
		print  trains
		return rows,source_cn,to_cn,date

	def buy_ticket(self,secretStr,source,to,date):
		buy_ticket_url='https://kyfw.12306.cn/otn/confirmPassenger/initDc'
		headers_checkUser={
			'Accept':'*/*',
			'Accept-Encoding':'gzip, deflate',
			'Accept-Language':'zh-CN,zh;q=0.8',
			'Cache-Control':'no-cache',
			'Connection':'keep-alive',
			# 'Content-Length':'10',
			'Content-Type':'application/x-www-form-urlencoded',
			'Host':'kyfw.12306.cn',
			'If-Modified-Since':'0',
			'Origin':'https://kyfw.12306.cn',
			'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
			'X-Requested-With':'XMLHttpRequest'
		}

		headers_sOR={
			'Accept':'*/*',
			'Accept-Encoding':'gzip, deflate',
			'Accept-Language':'zh-CN,zh;q=0.8',
			'Connection':'keep-alive',
			# 'Content-Length':'10',
			'Content-Type':'application/x-www-form-urlencoded',
			'DNT':'1',
			'Host':'kyfw.12306.cn',
			'Origin':'https://kyfw.12306.cn',
			'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
			'X-Requested-With':'XMLHttpRequest'
				}

		headers_initDC={
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate',
			'Accept-Language':'zh-CN,zh;q=0.8',
			'Cache-Control':'max-age=0',
			'Connection':'keep-alive',
			# 'Content-Length':'10',
			'Content-Type':'application/x-www-form-urlencoded',
			'Host':'kyfw.12306.cn',
			'Origin':'https://kyfw.12306.cn',
			'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
						}
		data={
			'secretStr':unquote(secretStr),
			'train_date':date,
			'back_train_date':time.strftime('%Y-%m-%d', time.localtime(time.time())), #today
			'tour_flag':'dc',
			'purpose_codes':'ADULT',
			'query_from_station_name':source,
			'query_to_station_name':to,
			'undefined':None,
				}
		# print data
		r=self.session.post(url='https://kyfw.12306.cn/otn/login/checkUser',headers=headers_checkUser,data={'_json_att':''})
		print r.content
		r=self.session.post(url='https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest',headers=headers_sOR,data=data)
		print r.content
		r=self.session.post(url='https://kyfw.12306.cn/otn/confirmPassenger/initDc',headers=headers_initDC,data={'_json_att':''})
		print r.content
		pattern='.*?globalRepeatSubmitToken = (.*?);.*?'
		m = re.match(pattern,repr(r.content))
		print m.group(1)
		return m.group(1)
if __name__=='__main__':
	log=login12306()
	while log.check_captcha()!=True:
		pass
	while log.login()!=True:
		time.sleep(1)

	tickets_imfor,source_cn,to_cn,date=log.left_ticket_imfor()
	train_no=raw_input('\n欲购车次为 :'.decode('utf-8').encode('gbk')).upper()
	tickets_imfor=[i.split('|') for i in tickets_imfor]
	for ticket in tickets_imfor:
		# print ticket[3],train_no
		if ticket[3]==train_no:
			secretStr=ticket[0]
			break

	# print unquote(secretStr)
	# print source_cn,to_cn
	# print {'aa':source_cn,'bb':to_cn}
	while log.buy_ticket(secretStr,source_cn,to_cn,date)=='null':
		time.sleep(1)
