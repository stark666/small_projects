#coding=gbk
#实现多个关键词搜索，基于数据库
import wmi,os,time,sqlite3,re


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
			elif os.path.isfile(path):
				count=0
				words=re.split('\s*',keywords)
				#print words
				for word in words:
					if word.lower() in x.lower():
						count+=1
				if count == len(words):
					print path
	except:
		pass


def choose_disks(disks):
	for i in range(len(disks)):
		print '[',i+1,']',disks[i],'\t',

	disks_choose=raw_input('\n\nwhich disks?\n')
	disks_choose_new=[]
	disks_list=list(disks_choose)

	if re.match('[0-9]*',disks_choose):
		#print 'num'
		for i in range(len(disks_list)):
			disks_choose_new.append(disks[i])
	elif re.match('[a-z]*',disks_choose.lower()):
		disks_choose_new=disks_list
	else:
		print 'wrong'

	for i in range(len(disks_list)):
		if disks_choose_new[i].upper() not in ''.join(disks):
			#print disks_choose_new[i], 'is legal'
			disks_choose_new.remove(disks_choose_new[i])
	return disks_choose_new


if __name__=='__main__':
	
	while True:
		
		print disks
		print type(disks)

		print "="*120
		choose_1=raw_input('fast search,slow search or update?(please update if first time using) f/s/u\n')
		

		if choose_1 == 'f':
			print "="*120
			keywords=raw_input('keywords: ')
			keywords=re.split('\s*',keywords)
			disks_list=choose_disks(disks)

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
				count=0
				for keyword in keywords:
					if keyword.lower().decode('gbk') in i[0].lower():
						count+=1
				if count == len(keywords):
					print i[0],'\n'

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
		

		
	

		
		