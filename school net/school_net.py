#coding=utf-8
#校园网登陆，未登陆打开登陆，登陆打开退出

import requests,json,socket
  
  
def log(status):  
    session = requests.session()  
    # res = session.get('http://my.its.csu.edu.cn/').content  
    session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
    }
    login_data = {  
        'username': '220161190',  
        'password': 'MjU5NzkxOXlZ',  
        'enablemacauth': 0 
    }  
    if status=='in':
        r=session.post('http://w.seu.edu.cn/index.php/index/login', data=login_data)
    elif status=='out':
        r=session.post('http://w.seu.edu.cn/index.php/index/logout', data=login_data)
    # res = session.get('http://w.seu.edu.cn/')  
    # print '*'*20
    # print r.status_code
    # print r.url
    res = session.get('http://w.seu.edu.cn/index.php/index/login') 
    # print type(res.text) 
    print json.loads(res.text)['info']

if __name__=='__main__':
    hostname=socket.gethostname()
    if hostname!='DESKTOP-N5B951A':
        exit(0)
    session = requests.session() 
    res = session.get('http://w.seu.edu.cn/index.php/index/login')
    if len(json.loads(res.text)['info'])==15:
        log('in')
        # session.headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
        # }
        # login_data = {  
        # 'username': '220161190',  
        # 'password': '*****',  
        # 'error_info':None
        # } 
        # r=session.post('https://selfservice.seu.edu.cn/selfservice/service_manage_status_web.php', data=login_data)
        # print r.content
    elif len(json.loads(res.text)['info'])==5:
        log('out')

