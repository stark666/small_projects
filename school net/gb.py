#coding=utf-8
# import cookielib  
# import urllib2  
# import urllib  
import requests,re,time,json
from bs4 import BeautifulSoup

# postdata1 = urllib.urlencode({  
#     'username': '220161190',  
#     'password': '2597919yY',
#     'error_info':None
# })  


session = requests.session()
session.headers = {          #手机版
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Proxy-Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded',
    # 'Cookie':'think_language=zh-CN; PHPSESSID=j9t3olkvr35qh0naghdbm0hb36',
    # 'Cookie':'PHPSESSID=u4n3t8o7vcks0ekfcud5eaa7e4; sunriseUsername=220161190; think_language=zh-CN',
    'DNT': '1',
    'Host':'w.seu.edu.cn',
    'Origin':'http://w.seu.edu.cn',
    'Referer':'http://w.seu.edu.cn/',
    'User-Agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36',
    'X-Requested-With':'XMLHttpRequest'
    }

login_data = {  
    'username': '220161190',  
    'password': 'MjU5NzkxOXlZ',  
    'enablemacauth': 1
} 
loginUrl='http://w.seu.edu.cn/index.php/index/login'
session.post(loginUrl, data=login_data)
res=session.get(loginUrl)
# session.cookies.save(ignore_discard=True,ignore_expires=True)
print json.loads(res.text)['info']





    # res = session.get('http://my.its.csu.edu.cn/').content  
session.headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
}
login_data = {  
    'username': '220161190',  
    'password': '*********',  
    'error_info':None
}  

r=session.post('https://selfservice.seu.edu.cn/selfservice/campus_login.php', data=login_data)
res = session.get('https://selfservice.seu.edu.cn/selfservice/service_manage_status_web.php') 
# soup=BeautifulSoup(res.content,'lxml')
pattern = re.compile(r'<td class="font_text" align="center">(.*?)</td>',  re.S) 
title = re.findall(pattern, res.content)
print ''
print title[0]

pattern = re.compile(r'<td width="30%" align="right" bgcolor="#FFFFFF">(.*?)&nbsp;&nbsp;</td>',  re.S) 
GB = re.findall(pattern, res.content)
print ''
print '本月使用校园网流量： '.decode('utf_8'),GB[0]
print ''
print '本月剩余校园网流量： '.decode('utf_8'),GB[1]
time.sleep(5)