#coding=gbk
#添加有道翻译
#添加aiml AI
import itchat, time,aiml,os,json,urllib2
from itchat.content import *


def youdao(words):
	#print type(words)
	#words=words.encode("utf-8")
	words=unicode(words, 'gbk')
	words=words.encode("UTF-8")
	qword = urllib2.quote(words)
	baseurl =r'http://fanyi.youdao.com/openapi.do?keyfrom=hitonystark&key=2023711410&type=data&doctype=json&version=1.1&q='
	url = baseurl+qword
    #print url
	resp = urllib2.urlopen(url)
	fanyi = json.loads(resp.read())
    #print fanyi
	if fanyi['errorCode'] == 0:        
        #if 'basic' in fanyi.keys():
	    trans =''.join(fanyi['translation'])
	    return trans

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
	zm= msg['Text']
	#print type(msg['Content'])
	#print type(zm)
	#word1=zm.encode("utf-8")
	words=zm.encode('gbk')


	#print type(word1)
	#print type(word2)
	#print word1
	#print word2

	word1=youdao(words)
	word2=alice.respond(word1)
	word4=youdao(word2)

	#if msg['FromUserName']!=msg['ToUserName']:
	if msg['FromUserName']!=msg['ToUserName']:
		#itchat.send('%s' %  alice.respond(msg['Text']), msg['FromUserName'])
		itchat.send(word4, msg['FromUserName'])
	#print len(msg['FromUserName'])

	#print msg['ToUserName']
	#print msg['FromUserName']
	#print msg['UserName']
	#print msg['Status']
	#print msg['RecommendInfo']['NickName']
	#print msg['Text']
	#print msg['RecommendInfo']
	#print msg['Content']
	


os.chdir('./alice')
alice=aiml.Kernel()
alice.learn('startup.xml')
alice.respond('LOAD ALICE')

#itchat.auto_login(hotReload=True)
itchat.auto_login(enableCmdQR=True)
itchat.auto_login(True)
itchat.run()

