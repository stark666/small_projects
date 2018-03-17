import wmi,os,re

c=wmi.WMI()
disks=[]

for physical_disk in c.Win32_DiskDrive (): 
	for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"): 
		for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"): 
			disks.append(logical_disk.Caption+os.path.sep) 

print '\n'

def choose_disks(disks):
	for i in range(len(disks)):
		print '[',i+1,']',disks[i],'\t',

	disks_choose=raw_input('\n\nwhich disks?\n')
	disks_choose_new=[]
	disks_list=list(disks_choose)

	if re.match('[0-9]+',disks_choose):
		print 'num'
		for i in range(len(disks_list)):
			disks_choose_new.append(disks[int(disks_list[i])-1])
	elif re.match('[a-z]+',disks_choose.lower()):
		#print 'letter'
		#print disks_list,disks_choose
		for i in range(len(disks_list)):
			if disks_list[i].upper()+':\\' in disks:
				disks_choose_new.append(disks_list[i].upper()+':\\')

	else:
		print 'wrong'


	return disks_choose_new


		
if __name__=='__main__':
	print choose_disks(disks)
