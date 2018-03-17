#coding=utf-8
# import cookielib  
# import urllib2  
# import urllib  
import requests,re,time,json
from bs4 import BeautifulSoup

# postdata1 = urllib.urlencode({  
#     'username': '220161190',  
#     'password': '*********',
#     'error_info':None
# })  


session = requests.session()

 
session.headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
}
login_data = {  
    'username': '220161190',  
    'password': '******',  
    'error_info':None
}  

r=session.post('https://selfservice.seu.edu.cn/selfservice/campus_login.php', data=login_data)
res = session.get('https://selfservice.seu.edu.cn/selfservice/service_recharge_rfid.php') 
# soup=BeautifulSoup(res.content,'lxml')
print res.headers
for i in res.history:
    print i