#coding=gbk
#插入排序 扑克牌洗牌

import random,time

def test(count,min,max):
	test=[]
	for i in range(count):
		test.append(random.randint(min,max))
	return test

while True:

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

	for i in range(len(num)):
		num[i]=int(num[i])

	time_1=time.time()
	for i in range(1,len(num)):
		for j in range(i):
			if num[i]<num[j]:
				num[:i+1]=num[:j]+[num[i]]+num[j:i]
				break
	time_2=time.time()
	print 'time:',time_2-time_1
				
	
	print '\nsort: ',num
	print ''
