#coding=utf-8
#登陆三星盖乐世论坛，并回复帖子
#我的ID：6356268，6359933。10604648.  398   1503
#中文匹配
#pid=228977

#添加首页标题关注 20171231

import requests,json,time,random,re,os
from urllib import quote,urlopen
from bs4 import BeautifulSoup
from ss import check
from colored import cs
from email4 import *

def log(username='18362966231',password='2597919yY'):  
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
        'EmailOrPhone': username,  
        'PwdErrorNum': '0',  
        'Pwd': password,
        'ImgCode':'' 
    }  

    r=session.post('https://www.galaxyclub.cn/login/index', data=login_data)

    tmp = session.get('http://www.galaxyclub.cn/mygalaxy')
    soup = BeautifulSoup(tmp.text, 'lxml')
    print '\n',soup.title.string,'\n'

    check(session)

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
            print cs('green','签到成功.\n'.decode('utf-8'))
            print '盖乐世论坛今日已领金币%s个\n'.decode('utf-8')%daily_coin

        # print res.text.encode('GB18030')
    else:
        print cs('yellow',json.loads(res.text)['Error']+'\n')

    return session        #登陆

def url_select(session):


	# reply(session,'看看')
	tmp = session.get('http://www.galaxyclub.cn/bbs/galaxys_s7-p1.html')
	# print tmp.content.decode('utf-8').encode('GB18030')
	soup = BeautifulSoup(tmp.text, 'lxml')
	
	url_group=[]

	# for i in soup.findAll(class_="tit",target="_blank"):               #改版前方法
	for i in soup.findAll(style="cursor: pointer;",target="_blank"):     #改版后
		post_data={}
		# post_data['Area']='%3Cp%3E'+quote(content)+'%3Cbr%2F%3E%3C%2Fp%3E'
		post_data['Title']=i.text
		post_data['href']='https://www.galaxyclub.cn'+i.get('href')
		pattern=r'/thread-(\d+)-(\d+)-(\d+).html'
		m = re.match(pattern,i.get('href'))
		post_data['Tid']=m.group(3)
		post_data['Fid']=m.group(2)
		post_data['Pid']=m.group(1)

		tmp = session.get(post_data['href'])
		# print tmp.content.decode('utf-8').encode('GB18030')
		soup_tmp = BeautifulSoup(tmp.text, 'lxml')
		value_tmp=soup_tmp.find('input',attrs={'type':"hidden",'name':'__RequestVerificationToken'})
		post_data['__RequestVerificationToken']=value_tmp.get('value')
		url_group.append(post_data)
		# break

	return url_group        #爬将要阅读的帖子的相关数据

def reply(session,data,content):

	print '正在回复'.decode('utf-8'),data['Title'],'\n'

   	post_data={
	    'Id':'0',
		'Pid':data['Pid'],
		'Area':'%3Cp%3E'+quote(content)+'%3Cbr%2F%3E%3C%2Fp%3E',
		             # %e6%94%af%e6%8c%81%e6%94%af%e6%8c%81
		'Code':'',
		'Tid':data['Tid'],
		'Fid':data['Fid'],
		'Title':data['Title'],
		'IsAuthorSee':False,
		'__RequestVerificationToken':data['__RequestVerificationToken'],
	}

   	r=session.post('http://www.galaxyclub.cn/BBS/SubReply', data=post_data)
    # print r.text
   	if json.loads(r.text)['State']==True and json.loads(r.text)['Data']['State']==False:
		print json.loads(r.text)['Data']['Message'],'\n'
    	# check(session)
    	# exit()
    	print 'ok'
    	return 'full'     #回复帖子随机内容


def daily_check(session):
	r=session.get('http://www.galaxyclub.cn/mygalaxy/MyTask')
	# print repr(r.content)
	# print r.content
	done_tmp=re.findall(u'<ul class="Mstoday">.*?</ul>',repr(r.text))
	# print done_tmp[0]
	# for i in done_tmp[0]:
	# 	print i,',',
	done_tmp[0]=done_tmp[0].replace(u'\\r\\n','')
	
	done=re.findall(u'<div>([\\u4e00-\\u9fa5]+)</div>\s+<a href="#" class="Comp">([\\u4e00-\\u9fa5]+)</a>',done_tmp[0])
	# print done
	undone=re.findall(u'<div>([\\u4e00-\\u9fa5]+)</div>\s+<a href="[a-z\/]+">([\\u4e00-\\u9fa5]+)</a>',done_tmp[0])
	# # print repr(r.text)
	for i in done:
		print i[0].decode("unicode-escape"),cs('green',i[1].decode("unicode-escape"),'bright')
	for j in undone:
		print j[0].decode("unicode-escape"),cs('red',j[1].decode("unicode-escape"),'bright')

def star_store(session):
	r=session.get(r'http://www.galaxyclub.cn/exchange')
	gifts=re.findall(u'<dd onclick="productLink\(\d{3}\);"><a>([\\u4e00-\\u9fa5]+)</a></dd>.*?<dd>(.*?)</dd>',repr(r.text))
	for gift in gifts:
		print gift[0].decode("unicode-escape"),'\t',cs('green',gift[1].decode("unicode-escape"),'bright')

	try:
		os.mkdir(r'C:\Users\yjh\a\spider\dist\star_store')
	except:
		pass

	
	with open(r'C:\Users\yjh\a\spider\dist\star_store\star_store.txt','w+') as f:
		for gift in gifts:
			f.write(gift[0].decode("unicode-escape").encode('utf-8')+'\n')
		f.close()


	with open(r'C:\Users\yjh\a\spider\dist\star_store\star_store_old.txt','rb') as f_old:
		foldread=f_old.read().decode('utf-8')
		f_old.close()
	with open(r'C:\Users\yjh\a\spider\dist\star_store\star_store.txt','rb') as f:
		fread=f.read().decode('utf-8')
		f.close()


	if fread==foldread:
		os.remove(r'C:\Users\yjh\a\spider\dist\star_store\star_store.txt')
		print 'equal'
	else:
		email_send('sir, there is something new on samsung star store.'+'\n'*2
					+fread+'\n'*2+'url= http://www.galaxyclub.cn/exchange'
					)		
		os.remove(r'C:\Users\yjh\a\spider\dist\star_store\star_store_old.txt')
		os.rename(r'C:\Users\yjh\a\spider\dist\star_store\star_store.txt',
					r'C:\Users\yjh\a\spider\dist\star_store\star_store_old.txt')
		print 'unequal'

# session=log()
# star_store(session)
# daily_check(session)

# url_group=url_select(session)
# # print url_group

# for data in url_group:
# 	reply_contents=['看看','不错不错','支持支持','看一下吧']
# 	content=random.choice(reply_contents)
# 	reply(session,data,content)
# 	break
print cs('cyan',u'有新礼品上架！','bright'),'\n'