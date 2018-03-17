#coding=UTF-8
#主要添加限定好友可以开启本计算机摄像头拍照功能
#添加录音功能，任意时长
import itchat,time,re,record
from itchat.content import *
from VideoCapture import Device

permission_name=['楊嘉豪'.decode('utf-8'),'Dora'.decode('utf-8')]
permission=False
king=''


#@itchat.msg_register([RECORDING, MAP, CARD, NOTE, SHARING])
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
	global permission_name,permission,king

	# print msg['Content'][:2]
	cam=Device()

	if msg['Content'][:3]=='发送给'.decode('utf-8') and msg['FromUserName']==king:
		# try:
		pattern='发送给'.decode('utf-8')+u'([\u4e00-\u9fa5]+)\s+([\u4e00-\u9fa5\,\?\，\？\.\。]+)'
		m=re.match(pattern,msg['Content'])
		print m.group(1),m.group(2)
		user=itchat.search_friends(name=m.group(1))[0]

		if m.group(2)=='拍照'.decode('utf-8'):
			cam.saveSnapshot('demo.jpg', quality=100, timestamp=4)
			user.send_image('demo.jpg')
			print '12'
			return
		elif m.group(2)=='连拍'.decode('utf-8'):
			for i in range(6):
				cam.saveSnapshot('demo'+str(i)+'.jpg', quality=100, timestamp=4)
				user.send_image('demo'+str(i)+'.jpg')
				time.sleep(1)
			return

		print type(user)
		print '1'
		user.send(m.group(2))
		print '2'
		return
		# except Exception,e:
		# 	print e
		# finally:
		# 	return


	# if msg['Content']=='发送拍照'.decode('utf-8') and msg['FromUserName']==msg['ToUserName']

	for i in msg:
		print i,msg[i]
	# print '\n',itchat.search_friends(userName=msg['FromUserName'])[0],': ',msg['Content'],'\n'
	# print '*'*120
	if msg['FromUserName']==msg['ToUserName']:
		king=msg['FromUserName']

	if msg['Content']=='给权限'.decode('utf-8') and msg['FromUserName']==msg['ToUserName']:
		permission=True
		# king=msg['FromUserName']
		itchat.send('ok, sir',msg['ToUserName'])
		return
	elif msg['Content']=='去权限'.decode('utf-8') and msg['FromUserName']==msg['ToUserName']:
		permission=False
		itchat.send('ok, sir',msg['ToUserName'])
		return

	if msg['Content']=='拍照'.decode('utf-8') and msg['User']['NickName'] in permission_name:
		try:
			# cam=Device()
			# cam.setResolution(640,480)
			cam.saveSnapshot('demo.jpg', quality=100, timestamp=4)
			itchat.send_image('demo.jpg',msg['FromUserName'])
			# return
		except Exception,e:
			print e
			# cam=Device()
			# cam.setResolution(640,480)
			cam.saveSnapshot('demo.jpg', quality=100, timestamp=4)
			itchat.send_image('demo.jpg',msg['FromUserName'])
		finally:
			return

	if msg['Content']=='给权限'.decode('utf-8') and permission==True:
		print '\n\n\nok\n\n\n'
		permission_name.append(msg['User']['NickName'])
		permission_name=list(set(permission_name))
		itchat.send('permission granted',msg['ToUserName'])
		return

	if msg['Content']=='去权限'.decode('utf-8') and permission==True:
		print '\n\n\nok\n\n\n'
		permission_name.remove(msg['User']['NickName'])
		itchat.send('permission granted',msg['ToUserName'])
		return


	if msg['Content']=='谁有权限'.decode('utf-8') and msg['FromUserName']==msg['ToUserName']:
		name_list=''
		for i in permission_name:
			name_list+=i+'\t'
		itchat.send(name_list,msg['ToUserName'])
		return

	# for i in permission_name:
	# 	print i,
	# print ''

	if msg['Content'][:2]=='连拍'.decode('utf-8') and msg['User']['NickName'] in permission_name:
		try:
			pattern='连拍'.decode('utf-8')+'\s*(\d+)'
			m=re.match(pattern,msg['Content'])
			
			if m==None:
				num=6
			else:
				num=int(m.group(1))
				if num<2:
					num=2

			for i in range(num):
				cam.saveSnapshot('demo'+str(i)+'.jpg', quality=100, timestamp=4)
				itchat.send_image('demo'+str(i)+'.jpg',msg['FromUserName'])
				time.sleep(1)
			# return
		except Exception,e:
			print e
			
			# cam.setResolution(640,480)
			for j in range(i,num):
				cam.saveSnapshot('demo'+str(j)+'.jpg', quality=100, timestamp=4)
				itchat.send_image('demo'+str(j)+'.jpg',msg['FromUserName'])
				time.sleep(1)
		finally:
			return


	if msg['Content'][:2]=='录音'.decode('utf-8') and msg['FromUserName']==king:
		try:
			pattern='录音'.decode('utf-8')+'\s*(\d+)'
			m=re.match(pattern,msg['Content'])
			
			if m==None:
				sec=10
			else:
				sec=int(m.group(1))
				if sec<5:
					sec=5

			itchat.send('recording...',msg['ToUserName'])
			record.Record(sec)
			itchat.send('done',msg['ToUserName'])
			itchat.send_file('output.wav',msg['ToUserName'])

		except Exception,e:
			print e
			itchat.send(e,msg['ToUserName'])
		finally:
			return
	# if msg['FromUserName'] in customer:
	# 	sec=random.uniform(0,2)
	# 	time.sleep(sec)
	# 	itchat.send(words['text'], msg['FromUserName'])

itchat.auto_login(enableCmdQR=True)
itchat.auto_login(True)
itchat.run()