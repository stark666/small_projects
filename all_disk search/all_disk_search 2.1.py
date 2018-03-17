#coding=gbk
#实现多个关键词代码搜索，基于数据库
import wmi,os,time,sqlite3,re


c=wmi.WMI()
disks=[]



#for physical_disk in c.Win32_DiskDrive (): 
#	for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"): 
#		for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"): 
#			disks.append(logical_disk.Caption+os.path.sep) 

def search(keycodes,dir):
	global sql
	try:

		for x in os.listdir(dir):
			path=os.path.join(dir,x)
			#print type(path)
			if sql == False:
				cursor.execute("insert into codesdb(path) values('%s')"%path.decode('gbk'))
			#print path
			if os.path.isdir(path):
				search(keycodes,path)
			elif os.path.splitext(path) == '.py':
				count=0
				words=re.split('\s*',keycodes)
				with open(path) as f:
					for code in f.readlines():
						for word in words:
							if word.lower() in code.strip().lower():
								count+=1
						if count == len(words):
							print path
	except:
		pass
#	for x in os.listdir(dir):
#		path=os.path.join(dir,x)
#		cursor.execute("insert into codesdb values('%s')"%path)
#			#print path
#		if os.path.isdir(path):
#			search(keycodes,path)
#		elif keycodes in x.lower():
#				
#			print path
			


#search('py','d:')

#a='d:'
#print type(a)
#print os.listdir(a)
#for i in range(len(disks)):
#	path=disks[i]
#	path=str(path)
#	print path
#
#	print os.listdir(path)


if __name__=='__main__':
	
	while True:
		

		print "="*120
		print '\ncodes search\n'
		choose_1=raw_input('fast search,slow search or update?(please update if first time using) f/s/u\n')
		

		if choose_1 == 'f':
			print "="*120
			keycodes=raw_input('keycodes: ')

			
			keycodes=re.split('\s*',keycodes)

			sql=True
			conn=sqlite3.connect('test.db')
			cursor=conn.cursor()
			#cursor.execute('delete from codesdb')
			#cursor.execute('create table if not exists codecodesdb (codes varchar(128))')
			cursor.execute('select * from codecodesdb')
			
			data=cursor.fetchall()
			#print len(data)
			time_1=time.time()
			for i in data:
				count=0
				for keycode in keycodes:
					if keycode.lower().decode('gbk') in i[0].lower():
						count+=1
				if count == len(keycodes):
					print i[0],'\n'

			time_2=time.time()
			print 'all disks costs',time_2-time_1,'s \n'
			cursor.close()
			conn.close()
		elif choose_1 == 's':
			print "="*120
			keycodes=raw_input('keycodes: ')
			sql=True
			sec=0
			
			path=r'C:\Users\yjh01\a'
			#path=str(path)
			print 'start searching ',path
			time_1=time.time()
			search(keycodes,path)
			time_2=time.time()
			sec+=time_2-time_1
			print '\n%s costs '%path,time_2-time_1,'s \n'
			print sec,'s in total'

		elif choose_1 == 'u':
			sql=False
			print 'updating ... about 10 mins, please wait'
			conn=sqlite3.connect('test.db')
			cursor=conn.cursor()
			cursor.execute('create table if not exists codesdb (path varchar(128))')
			cursor.execute('delete from codesdb')
			cursor.execute('create table if not exists codesdb (path varchar(128))')
			
			for i in range(len(disks)):
				
				path=r'C:\Users\yjh01\a'
				#path=str(path)
				time_1=time.time()
				search('gdgdfgdfdfgdfdggbbs',path)
				time_2=time.time()
				
				print '\n%s costs '%path,time_2-time_1,'s \n'
				print 'done'

			conn.commit()
			cursor.close()
			conn.close()
		else:
			continue


			#print disks
		

		
	

		
		