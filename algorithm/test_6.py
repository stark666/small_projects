#coding=gbk
#ϣ���㷨

import time,random

def test(count,min,max):
	test=[]
	for i in range(count):
		test.append(random.randint(min,max))
	return test

def insert_sort(lists):
	for i in range(1,len(lists)):
		for j in range(i):
			if lists[i]<lists[j]:
				lists[:i+1]=lists[:j]+[lists[i]]+lists[j:i]
				break
	return lists

def shell(lists,num):
	count=len(lists)
	step=count/2

	while step!=0:
		#print '\nstep:',step
		for i in range(step):
			new_num=[]
			new_lists=[]
			index=i
			while index<count:
				new_num.append(index)
				index+=step
			for j in new_num:
				new_lists.append(lists[j])
			new_lists=insert_sort(new_lists)
			h=0
			#print '\nbefore:',lists
			for k in new_num:
				lists[k]=new_lists[h]
				h+=1
			#print '\nafter:',lists
			#print ''
		
		step/=2
	return lists

if __name__=='__main__':
	num=raw_input('\nnumbers list: ')
	print ''
	num=filter(lambda x:x!='',num.split(' '))
	if num[0]=='test':
		num=test(int(num[1]),int(num[2]),int(num[3]))
	elif num[0]=='range':
		num=range(int(num[1]))

	else:
		for i in range(len(num)):
			num[i]=int(num[i])

	lists=num

	time_1=time.time()
	num=range(len(lists))
	lists=shell(lists,num)
	time_2=time.time()
	print 'time:',time_2-time_1
				
	print lists
	#print '\nsort: ',num
	print ''

			