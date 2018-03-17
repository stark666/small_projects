#coding=gbk
#实现单个关键词搜索，基于数据库
import wmi,os,time,sqlite3


c=wmi.WMI()
disks=[]



for physical_disk in c.Win32_DiskDrive (): 
	for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"): 
		for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"): 
			disks.append(logical_disk.Caption+os.path.sep) 

def search(keywords,dir):
	global sql
	try:

		for x in os.listdir(dir):
			path=os.path.join(dir,x)
			#print type(path)
			if sql == False:
				cursor.execute("insert into sdb(path) values('%s')"%path.decode('gbk'))
			#print path
			if os.path.isdir(path):
				search(keywords,path)
			elif keywords.lower() in x.lower():
				
				print path
	except:
		pass
#	for x in os.listdir(dir):
#		path=os.path.join(dir,x)
#		cursor.execute("insert into sdb values('%s')"%path)
#			#print path
#		if os.path.isdir(path):
#			search(keywords,path)
#		elif keywords in x.lower():
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
		choose_1=raw_input('fast search,slow search or update?(please update if first time using) f/s/u\n')
		

		if choose_1 == 'f':
			print "="*120
			keywords=raw_input('keywords: ')
			sql=True
			conn=sqlite3.connect('test.db')
			cursor=conn.cursor()
			#cursor.execute('delete from sdb')
			#cursor.execute('create table if not exists sdb (path varchar(128))')
			cursor.execute('select * from sdb')
			
			data=cursor.fetchall()
			#print len(data)
			time_1=time.time()
			for i in data:
				if keywords.lower().decode('gbk') in i[0].lower():
					print i[0]
			time_2=time.time()
			print 'all disks costs',time_2-time_1,'s \n'
			cursor.close()
			conn.close()
		elif choose_1 == 's':
			print "="*120
			keywords=raw_input('keywords: ')
			sql=True
			sec=0
			for i in range(len(disks)):
				path=disks[i]
				path=str(path)
				print 'start searching ',path
				time_1=time.time()
				search(keywords,path)
				time_2=time.time()
				sec+=time_2-time_1
				print '\n%s costs '%path,time_2-time_1,'s \n'
			print sec,'s in total'

		elif choose_1 == 'u':
			sql=False
			print 'updating ... about 10 mins, please wait'
			conn=sqlite3.connect('test.db')
			cursor=conn.cursor()
			cursor.execute('create table if not exists sdb (path varchar(128))')
			cursor.execute('delete from sdb')
			cursor.execute('create table if not exists sdb (path varchar(128))')
			
			for i in range(len(disks)):
				
				path=disks[i]
				path=str(path)
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
		

		
	

		
		