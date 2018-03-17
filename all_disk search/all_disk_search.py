import wmi,os,time


c=wmi.WMI()
disks=[]

for physical_disk in c.Win32_DiskDrive (): 
	for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"): 
		for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"): 
			disks.append(logical_disk.Caption+os.path.sep) 

def search(keywords,dir):
	try:

		for x in os.listdir(dir):
			path=os.path.join(dir,x)
			#print path
			if os.path.isdir(path):
				search(keywords,path)
			elif keywords in x.lower():
				
				print path
	except:
		pass
			


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


#if __name__ == '__main__':
while True:
	print disks
	keywords=raw_input('keywords: ')

	for i in range(len(disks)):
		path=disks[i]
		path=str(path)
		time_1=time.time()
		search(keywords,path)
		time_2=time.time()
		print '\n%s costs '%path,time_2-time_1,'s \n'