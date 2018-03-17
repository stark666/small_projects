#coding=utf-8
#登陆三星盖乐世论坛，并回复帖子
#我的ID：6356268，6359933。10604648.  398   1503
#中文匹配
import requests,json,time,random,re,os
from urllib import quote,urlopen
from bs4 import BeautifulSoup
from ss import check
from colored import cs

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
        'EmailOrPhone': '472217937@qq.com',  
        'PwdErrorNum': '0',  
        'Pwd': '************',
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


def read(session,data):
	print '正在阅读'.decode('utf-8'),data['Title'],'\n'

	r=session.post(r'https://www.galaxyclub.cn/BBS/GetCreditResult',data={'Pid':data['Pid']})
	# print r.text
	if json.loads(r.text)['State']==False: #您已经进行过评价
		print json.loads(r.text)['Error'],cs('green','您已经进行过评价'.decode('utf-8')+'\n')

   	if json.loads(r.text)['State']==True:     #阅读成功
		if json.loads(r.text)['Data']['State']==True:
			print cs('green','阅读成功\n'.decode('utf-8'))
    
		else:    #该操作当天获得积分/经验超过上限
			print cs('red',json.loads(r.text)['Data']['Message']+'\n')
	    	# check(session)
	    	# exit()
			return 'full'	      #阅读帖子


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
    	return 'full'     #回复帖子随机内容


def praise(session,data):

	print '正在点赞'.decode('utf-8'),data['Title'],'\n'

   	post_data={
	    'Id':'0',
		'Pid':data['Pid'],
		'Fid':data['Fid'],
		'Type':'thread'
	}

   	r=session.post('http://www.galaxyclub.cn/BBS/Praise', data=post_data)
   	# print r.text
   	if json.loads(r.text)['State']==False: #您已经进行过评价
		print cs('green',json.loads(r.text)['Error']+'\n')

	if json.loads(r.text)['State']==True:    
		if json.loads(r.text)['Data']['State']==True:  #点赞成功
			print cs('green',json.loads(r.text)['Error']+'\n')
    	
		else:    #该操作当天获得积分/经验超过上限
			print cs('red',json.loads(r.text)['Data']['Message'],'\n')
	    	# check(session)
	    	# exit()
			return 'full'         #点赞帖子


def url_select(session):


	# reply(session,'看看')
	tmp = session.get('http://www.galaxyclub.cn/bbs/galaxys_s7-p2.html')
	# print tmp.content.decode('utf-8').encode('GB18030')
	soup = BeautifulSoup(tmp.text, 'lxml')
	
	url_group=[]

	for i in soup.findAll(class_="tit",target="_blank"):
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


def star_store_2(session):
	r=session.get(r'http://www.galaxyclub.cn/exchange')
	# soup = BeautifulSoup(r.text, 'lxml')
	# print r.read().decode('utf-8').encode('GB18030')
	pattern=r'<dt onclick="productLink\(\d{3}\);">(.*?)</dt>'
              # <dt onclick="productLink(163);">【11月星粉周】天猫官旗500元优惠券</dt>
	m=re.findall(pattern,r.content)
	# m=re.findall(pattern,'<dt onclick="productLink(161);">【11月星粉周】</dt>')
	# print m[0].decode('utf-8')
	for i in m:
		print i.decode('utf-8')          


def star_store(session):
	r=session.get(r'http://www.galaxyclub.cn/exchange')
	soup = BeautifulSoup(r.text, 'lxml')
	# print r.read().decode('utf-8').encode('GB18030')
	gifts=soup.findAll(name='dt',attrs={'onclick':re.compile(r'productLink\(\d{3}\);')})

	try:
		os.mkdir('star_store')
	except:
		pass

	with open(r'C:\Users\yjh\a\spider\dist\star_store\star_store.txt','a+') as f:
		for i in gifts:
			# print type(i)
			# print repr(i.next_element.next_element)
			print i.string,'\t'*4,
			f.write(i.string.encode('GB18030')+'\n')
			for j in i.next_sibling.next_sibling.strings:             #实际文档中的tag的 .next_sibling 和 .previous_sibling 
				print j,
				# f.write(j.encode('GB18030'))                          #属性通常是字符串或空白，因为空白或者换行也可以被视作一个节点，
			# print ''                                                #所以得到的结果可能是空白或者换行
			print i.next_sibling.next_sibling.next_sibling.next_sibling.string
			# f.write(i.next_sibling.next_sibling.next_sibling.next_sibling.string.encode('GB18030')+'\n')
		
			print ''                                                  #爬星币商城物品
		f.flush()


		with open(r'C:\Users\yjh\a\spider\dist\star_store\star_store_old.txt','a+') as f_old:
			foldread=f_old.read()
			f.seek(0)
			fread=f.read()
			# print 'bbbb',fread
			if fread==foldread:
				f.close()
				os.remove(r'C:\Users\yjh\a\spider\dist\star_store\star_store.txt')
			else:
				# f.seek(0)
				email_send('sir, there is something new on samsung star store.'+'\n'*2
					+fread.decode('GB18030')+'\n'*2
					+'url= http://www.galaxyclub.cn/exchange'
					)
				with open(r'C:\Users\yjh\a\spider\dist\star_store\star_store_old.txt','w+') as f_new:
					# f.seek(0)
					f_new.write(fread)
					f_new.close()
					f.close()
					os.remove(r'C:\Users\yjh\a\spider\dist\star_store\star_store.txt')
			f_old.close()


def AddFollows(session):
	post_data={
	    'FollowUserId':'6359933'
	}
	r=session.post('http://www.galaxyclub.cn/shared/AddFollows', data=post_data)
	# print r.text
	if json.loads(r.text)['State']==False:
		r=session.post('http://www.galaxyclub.cn/shared/CancleFollows', data=post_data)
		# print r.text
		r=session.post('http://www.galaxyclub.cn/shared/AddFollows', data=post_data)
		# print r.text
	if json.loads(r.text)['State']==True:
		print cs('green','关注成功'.decode('utf-8'))
		return 'full'          #关注某人


def Share(session,data):
    post_data={
        'Oid':data['Pid'],  #411478
        'platform':'weixin'
    }
    r=session.post('http://www.galaxyclub.cn/Shared/Share', data=post_data)
    print r.text
    if json.loads(r.text)['State']==False: #您已经进行过评价
        print json.loads(r.text)['Error'],cs('green','您已经进行过分享'.decode('utf-8')+'\n')

    if json.loads(r.text)['State']==True:     #阅读成功
        if json.loads(r.text)['Data'] and json.loads(r.text)['Data']['State']==True:
            print cs('green','分享成功\n'.decode('utf-8'))
    
        else:    #该操作当天获得积分/经验超过上限
            print cs('red','该操作当天获得积分/经验超过上限\n'.decode('utf-8'))
            # check(session)
            # exit()
            return 'full'           #分享至朋友圈


def friendgalaxy(session,ID):                   #浏览好友首页
	t=session.get('http://www.galaxyclub.cn/friendgalaxy/'+str(ID))
	# print t.text.encode('GB18030')


def subpost(session):
	url='http://www.galaxyclub.cn/bbs/posting?Fid=33&PTId=0&Fid1=22'
	r=session.get(url)
	soup=BeautifulSoup(r.text,'lxml')
	value=soup.find('input',attrs={'type':"hidden",'name':'__RequestVerificationToken'})
	m=re.match(r'.*?([0-9a-z]{8}\-[0-9a-z]{4}\-[0-9a-z]{4}\-[0-9a-z]{4}\-[0-9a-z]{12}).*?',repr(r.text))
	# print m.group(1)
	post_data={}
	post_data['Token']=m.group(1)
	value=value.get('value')
	post_data['__RequestVerificationToken']=value
	# print r.text.encode('GB18030')
	# print repr(r.text.encode('GB18030'))
	m=re.match(r'http://www.galaxyclub.cn/bbs/posting\?Fid=(\d+)&PTId=(\d+)&Fid1=(\d+)',url)
	post_data['FId1']=str(m.group(3))
	post_data['FId']=str(m.group(1))
	post_data['PTId']=str(m.group(2))
	post_data['RequireIMEI']=False
	post_data['IsAuthorSee']=False
	post_data['FId2']=post_data['FId']
	post_data['TId']='42'
	post_data['Forumtype']='1'
	post_data['Img']=None
	post_data['Title']='十年前你在用什么手机'
	post_data['Content']='十年前我没有手机哈哈哈'
	post_data['ContentText']='%3Cp%3E'+quote(post_data['Content'])+'%3C%2Fp%3E'
	post_data['ImageCode']='7792'
	# print post_data
	r=session.post('http://www.galaxyclub.cn/bbs/SubPosting', data=post_data)
	thread=json.loads(r.text)['Error']

	print thread
	pattern=r'/thread-(\d+)-(\d+)-(\d+).html'
	m = re.match(pattern,thread)
	del_post_data={}
	del_post_data['Tid']=m.group(3)
	del_post_data['Fid']=m.group(2)
	del_post_data['Pid']=m.group(1)

	sec=random.uniform(10,30)
	print sec,'s to wait ...'
	time.sleep(sec)

	r=session.post('http://www.galaxyclub.cn/BBS/CheckShowDelResion', data=del_post_data)
	del_post_data['delResion']=None
	r=session.post('http://www.galaxyclub.cn/BBS/DelPost', data=del_post_data)
	# print r.text
	if json.loads(r.text)['State']==True:
		return 'full'          #发帖
 

def daily_misson(session):
	situ_5=subpost(session)
	situ_6=AddFollows(session)
	if situ_5=='full' and situ_6=='full':
		return 'full'         #完成每日任务
# http://www.galaxyclub.cn/shared/CancleFollows

def daily_check(session):
	r=session.get('http://www.galaxyclub.cn/mygalaxy/MyTask')
	done=re.findall(r'<li>([\u4e00-\u9fa5]+)<p class="fr">([\u4e00-\u9fa5]+)</p></li>',repr(r.text))
	undone=re.findall(u'<li>([\\u4e00-\\u9fa5]+)<span>([\\u4e00-\\u9fa5]+)</span></li>',repr(r.text))
	# print repr(r.text)
	for i in done:
		print i[0].decode("unicode-escape"),cs('green',i[1].decode("unicode-escape"),'bright')
	for j in undone:
		print j[0].decode("unicode-escape"),cs('red',j[1].decode("unicode-escape"),'bright')

# def check(session):
#     tmp = session.get('http://www.galaxyclub.cn/mygalaxy')
#     soup = BeautifulSoup(tmp.text, 'lxml')
#     for coin in soup.find_all('strong'):
#         # print coin.parent.get('class')[0]
#         try:
#             if coin.parent.get('class')[0]=='info3':
#                 coin_count=coin.string
#             elif coin.parent.get('class')[0]=='info4':
#                 exp_count=coin.string
#             elif coin.parent.get('class')[0]=='info5':
#                 sign_count=coin.string
#         except:
#             pass

#     print '已有金币%s个\n'.decode('utf-8')%coin_count
#     print '经验值%s\n'.decode('utf-8')%exp_count
#     print '已签到%s天\n'.decode('utf-8')%sign_count
#     print coin_count,exp_count,sign_count

if __name__=='__main__':
	session=log()

	
	if session:
		
		# AddFollows(session)

		url_group=url_select(session)
		# url_group=random.shuffle(url_group)

		print '正在浏览好友主页.\n'.decode('utf-8')
		for i in range(6356268,6356268+6):
			friendgalaxy(session,i)
			time.sleep(2)

		# data=url_group[6]
		# print url_group
		# test=session.post(r'https://www.galaxyclub.cn/BBS/GetCreditResult',data={'Pid':data['Pid']})
		# print test.text
		
		situ_daily=daily_misson(session)
		print situ_daily

		for data in url_group:
			situ_1,situ_2,situ_3,situ_4=None,None,None,None
			wait_time=random.uniform(10,30)

			# test=session.get(data['href'])
			# test=session.post(r'https://www.galaxyclub.cn/BBS/GetCreditResult',data={'Pid':data['Pid']})
			# print test.text
			situ_1=read(session,data)
			situ_2=praise(session,data)
			print wait_time,'s to wait\n'
			reply_contents=['看看','不错不错','支持支持','看一下吧']
			content=random.choice(reply_contents)
			time.sleep(wait_time)
			situ_4=Share(session,data)		
			situ_3=reply(session,data,content)			
			print '已回复'.decode('utf-8'),content.decode('utf-8')

			

			print situ_1,situ_2,situ_3,situ_4,situ_daily
			if situ_1 =='full' and situ_2=='full' and situ_3=='full' and situ_4=='full' and situ_daily=='full':
				break
			print '*'*120
			print ''

		daily_check(session)	
		star_store(session)

		check(session)

	os.system('pause')







