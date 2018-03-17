#coding=UTF-8
#添加图灵机器人API
#添加在已知位置基础上回复目前所处位置

import itchat, time,aiml,os,json,urllib2,urllib,random,sys
from xml.parsers.expat import ParserCreate
from itchat.content import *

first=True
myself=[]
baby='456'
customer=[]
contents=[]
location=''

class DefaultSaxHandler(object):
	def start_element(self, name, attrs):
		self.attrs = attrs
		#print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

	def returnattrs(self):
		return self.attrs



#@itchat.msg_register([RECORDING, MAP, CARD, NOTE, SHARING])
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
	global flag,myself,customer,first,contents,baby,location
	num=0

	print msg
	#print msg['Type']
	#msg['Text'](msg['FileName'])
	#itchat.send('@%s@%s'%('fil', msg['FileName']), msg['ToUserName'])



	zm= msg['Text']
	#print type(msg['Content'])
	#print type(zm)
	#word1=zm.encode("utf-8")
	words=zm.encode('UTF-8')
	#print words
	words2=zm.encode('gbk')
	#print words2

	url='http://www.tuling123.com/openapi/api'

	data={u'key':'9d937855ed1c42a19239984cd14af19d','info':words,u'loc':'','userid':''}
	data=urllib.urlencode(data)
	url2=urllib2.Request(url,data)
	resp=urllib2.urlopen(url2)
	apicontent=resp.read()
	words=json.loads(apicontent,encoding='UTF-8')


	#word1=youdao(words)
	#word2=alice.respond(word1)
	#word4=youdao(word2)

	#itchat.send('%s' %  alice.respond(msg['Text']), msg['FromUserName'])
	#if msg['ToUserName']==msg['FromUserName']:
		#itchat.send(words['text'], msg['FromUserName'])


	if msg['Type'] == 'Map':
		xml = msg['OriContent']
		#print xml
		xml = xml.encode('UTF-8')
		#print xml
		handler = DefaultSaxHandler()
		parser = ParserCreate()
		parser.returns_unicode = True
		parser.StartElementHandler = handler.start_element
		parser.Parse(xml)
		where=handler.returnattrs()
		
		location='我在'.decode('gbk')+where['poiname']+'\n'+where['label']
		print location
		return

	if (('你在哪' in msg['Content'].encode('gbk')) or ('宝宝在哪' in msg['Content'].encode('gbk'))) and msg['FromUserName'] not in myself:
		try:
			itchat.send(location,msg['FromUserName'])
			return
		finally:
			return

    
	if '是我' in msg['Content'].encode('gbk') and msg['ToUserName']==msg['FromUserName']:
		myself.append(msg['FromUserName'])
		itchat.send('At your service, sir', msg['ToUserName'])
		print msg['User']['NickName'].encode('gbk')


	if msg['FromUserName'] in myself:
		contents.append(msg['Text'])


	if '宝宝' in msg['Content'].encode('gbk') and msg['FromUserName'] in myself and first==True:
		baby=msg['ToUserName']
		#itchat.send('宝宝您好'.decode('gbk'), msg['ToUserName'])
		first=False
		return
	


	if '报警'==msg['Content'].encode('gbk') and msg['FromUserName'] in myself and msg['ToUserName'] ==baby and baby in customer:
		try:
			#print contents[-2]
			#print type(contents[-2])
			t=int(contents[-2].encode('gbk'))
			for i in range(t):
				
				itchat.send('阿宝在哪'.decode('gbk'), baby)
				time.sleep(2)
		except:
			itchat.send('报警失败'.decode('gbk'), baby)

		return

	

	if '给权限' in msg['Content'].encode('gbk') and msg['FromUserName'] == myself[0]:
		myself.append(msg['ToUserName'])
		itchat.send('Done, sir', msg['ToUserName'])
		return

	if '去权限' in msg['Content'].encode('gbk') and msg['FromUserName'] == myself[0]:
		for i in range(len(myself)):
			if msg['ToUserName']==myself[i]:
				del myself[i]
		
		itchat.send('OK, sir', msg['ToUserName'])
		return
	


	
	



	if '秘书过来' in msg['Content'].encode('gbk') and msg['FromUserName'] in myself:
		#print msg['ToUserName'].encode('gbk')
		if msg['FromUserName'] == myself[0]:
			customer.append(msg['ToUserName'])
			itchat.send('I\'m here, sir', msg['ToUserName'])
		else:
			customer.append(msg['FromUserName'])
			itchat.send('I\'m here, sir', msg['FromUserName'])
		return
		
		#flag=True
		#print flag

	if '我回来' in msg['Content'].encode('gbk') and msg['FromUserName'] in myself and msg['ToUserName'] in customer:
		if msg['FromUserName'] == myself[0]:
			for i in range(len(customer)):
				if msg['ToUserName']==customer[i]:
					del customer[i]
		
			itchat.send('see you, sir', msg['ToUserName'])
		else:
			for i in range(len(customer)):
				if msg['FromUserName']==customer[i]:
					del customer[i]
			itchat.send('see you, sir', msg['FromUserName'])
			
		return
	
		#flag=False

	if '骂他傻逼' in msg['Content'].encode('gbk') and msg['FromUserName'] in myself and msg['ToUserName'] in customer:
		while True:
			#text_reply(msg)
			while num<10:
				time.sleep(0.5)
				itchat.send('傻逼儿子'.decode('gbk'), msg['ToUserName'])
				num+=1
			break

		return


	if '想阿宝' in msg['Content'].encode('gbk') and msg['FromUserName'] in myself and msg['ToUserName'] in customer:
		while True:
			#text_reply(msg)
			while num<10:
				time.sleep(0.5)
				itchat.send('我想宝宝了'.decode('gbk'), msg['ToUserName'])
				num+=1
			break

		return





	if msg['FromUserName'] in customer:
		#if '傻逼' in msg['Content'].encode('gbk') and msg['FromUserName']==myself:
			#pass

		#elif '宝宝' in msg['Content'].encode('gbk') and msg['FromUserName']==myself:
			#pass

		#elif '报警' in msg['Content'].encode('gbk') and msg['FromUserName']==myself:
			#pass

	
		#else:
		sec=random.uniform(0,2)
		time.sleep(sec)
		itchat.send(words['text'], msg['FromUserName'])
			
			#if '好了' in msg['Content'].encode('gbk') and msg['FromUserName']==myself:
			#	print 'ok'
			#	break
			#print msg['Text']

#@itchat.msg_register(TEXT, isGroupChat=True)
#def text_reply(msg):
 #   if msg['isAt']:
 #       itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

	




#itchat.auto_login(enableCmdQR=0.5)
itchat.auto_login(enableCmdQR=True)
itchat.auto_login(True)
itchat.run()