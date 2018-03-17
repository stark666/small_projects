#coding=gbk
#实现单个关键词搜索，基于文本文档
import wmi,os,time,re


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
				f=open('test.txt','w')
				f.write(path)
				f.write('\n')
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
			keywords=re.split('\s*',keywords)
			sql=True
			f=open('test.txt')
			
			
			
			
			#print len(data)
			time_1=time.time()
			for i in f.readlines():
				count=0
				for keyword in keywords:
					if keyword.lower().decode('GB18030') in i.decode('GB18030').lower():
						count+=1
				if count == len(keywords):
					print i
			time_2=time.time()
			print 'all disks costs',time_2-time_1,'s \n'
			

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
	
			
			for i in range(len(disks)):
				
				path=disks[i]
				path=str(path)
				time_1=time.time()
				search('gdgdfgdfdfgdfdggbbs',path)
				time_2=time.time()
				
				print '\n%s costs '%path,time_2-time_1,'s \n'
				print 'done'


		else:
			continue


			#print disks
		

		
	

		
		