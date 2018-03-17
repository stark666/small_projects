#coding=gbk
import requests,re,time,json,prettytable



def colored(color, text):  
    table = {  
        'red': '\033[91m',  
        'green': '\033[92m',  
        # no color  
        'nc': '\033[0m'  
    }  
    cv = table.get(color)  
    nc = table.get('nc')  
    return ''.join([cv, text, nc]) 

station_code_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955"
        #去除https访问的警告信息
requests.packages.urllib3.disable_warnings()
r = requests.get(station_code_url, verify=False)
station_code_html = r.text



station_code = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', station_code_html)
station_code_dict = dict(station_code)


#station_code : [('北京东','VAP')，(...)，...]
#station_code_dict : {'北京东':'VAP'，...:...,}

#print station_code_dict.get('泉州'.decode('gbk'))

t=time.strftime("%Y-%m-%d", time.localtime())

date=raw_input('date:')
#source=raw_input('from:')
#to=raw_input('to:')
source=station_code_dict.get(raw_input('from:').decode('gbk'))
to=station_code_dict.get(raw_input('to:').decode('gbk'))

print source,to

#query_url = "https://kyfw.12306.cn/otn/leftTicket/log?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT"%(date,source,to)
#query_url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=%s&from_station=%s&to_station=%s'%(date,source,to)
query_url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'%(date,source,to)

ticket_imfor=requests.get(query_url,verify=False)
rows=ticket_imfor.json().get('data').get('result')
#
trains= prettytable.PrettyTable() 
row_1=['车次',"车站","时间","历时","商务座,特等座","一等座","二等座","高级软卧","软卧","硬卧 ","软座 ","硬座","无座"]
##for i in range(len(row_1)):
##	row_1[i]=row_1[i].encode('GB18030')
#trains.field_names=row_1

#test_0=rows[0].split('|')
#for index,item in enumerate(test_0):
#	print index,item
#
#test_9=rows[40].split('|')
#for index,item in enumerate(test_9):
#	print index,item
#
#test_2=rows[2].split('|')
#for index,item in enumerate(test_2):
#	print index,item
#
#test_4=rows[4].split('|')
#for index,item in enumerate(test_4):
#	print index,item

for row in rows :
#	row=row.encode('gbk')
	row=row.split('|')
#	print row
	trains.add_row([row[3], '\n'.join([colored('green', row[6]),  colored('red', row[7])]), '\n'.join([colored('green', row[8]),colored('red', row[9])]), row[10],row[32], row[31],row[30],row[21], row[23],row[28],row[24],row[29],row[26]])  

print trains


