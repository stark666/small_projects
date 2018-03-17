#coding=utf-8
#登陆三星盖乐世论坛，并自动签到
import requests,json,time
from bs4 import BeautifulSoup
import logging  
logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename=r'G:\log\samsung_galaxy_club\%s.log'%time.strftime("%Y-%m-%d", time.localtime()),  
                    filemode='w')

def log():  
    session = requests.session()  
    # res = session.get('http://my.its.csu.edu.cn/').content  
    session.headers = {
    'Connection': 'Keep-Alive',  
    'Accept-Language': 'zh-CN',  
    'Accept': '*/*',
    'DNT': '1' ,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',  
    'Accept-Encoding': 'gzip, deflate',  
    'X-Requested-With': 'XMLHttpRequest',  
    'Host': 'www.galaxyclub.cn',
    'Referer':'http://www.galaxyclub.cn/' 
    }
    login_data = {  
        'EmailOrPhone': '**********',  
        'PwdErrorNum': '0',  
        'Pwd': '********',
        'ImgCode':'' 
    }  

    r=session.post('https://www.galaxyclub.cn/login/index', data=login_data)

    tmp = session.get('http://www.galaxyclub.cn/mygalaxy')
    soup = BeautifulSoup(tmp.text, 'lxml')
    print '\n',soup.title.string,'\n'


    res=session.post('http://www.galaxyclub.cn/Shared/Sign')
    state=json.loads(res.text)['State']

    if state==True:    #登陆成功后进行签到先post一个再get一个
        daily_coin=int(json.loads(res.text)['Data']['CreditCount'])
        # +int(json.loads(res.text)['Data']['EmpricCount'])
        print '登陆成功.\n'.decode('utf-8')
        # print res.text.encode('GB18030')

        res = session.get('http://www.galaxyclub.cn/Shared/UserSign?ramdon=529') 

        state=json.loads(res.text)['Data']['IsSign']
        if state==True:
            print '签到成功.\n'.decode('utf-8')
            print '盖乐世论坛今日已领金币%s个\n'.decode('utf-8')%daily_coin

        # print res.text.encode('GB18030')
    else:
        print json.loads(res.text)['Error'],'\n'

    return session

def check(session):
    tmp = session.get('http://www.galaxyclub.cn/mygalaxy')
    soup = BeautifulSoup(tmp.text, 'lxml')
    for coin in soup.find_all('strong'):
        # print coin.parent.get('class')[0]
        try:
            if coin.parent.get('class')[0]=='info3':
                coin_count=coin.string
            elif coin.parent.get('class')[0]=='info4':
                exp_count=coin.string
            elif coin.parent.get('class')[0]=='info5':
                sign_count=coin.string
        except:
            pass

    print '已有金币%s个\n'.decode('utf-8')%coin_count
    print '经验值%s\n'.decode('utf-8')%exp_count
    print '已签到%s天\n'.decode('utf-8')%sign_count
    logging.info('已有金币%s个\n'.decode('utf-8')%coin_count)
    logging.info('经验值%s\n'.decode('utf-8')%exp_count)
    logging.info('已签到%s天\n'.decode('utf-8')%sign_count)
    logging.info('\n')


    # print coin_count,exp_count,sign_count

if __name__=='__main__':
    session=log()
    check(session)
    time.sleep(5)