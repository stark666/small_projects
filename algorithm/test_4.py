#coding=gbk
#��������

import random,time

def quicksort(num):
	key=0
	key_i=0
	key_j=len(num)

	while True:

		for j in range(key_j-1,-1,-1):
			if j==key_i:
				return num,key
			if num[j]<num[key]:
				num[j],num[key]=num[key],num[j]
				key_j=j
				key=j
				break

		for i in range(key_i+1,len(num)):
			if i==key_j:
				return num,key
			if num[i]>num[key]:
				num[i],num[key]=num[key],num[i]
				key_i=i
				key=i
				break

def singleitem(num):

	num,key=quicksort(num)
	num_1=num[:key]
	num_2=num[key+1:]
	num=[num_1,[num[key]],num_2]
	#print 'now num=',num
	for i in range(len(num)):
		if len(num[i])<=1:
			if len(num[i])==1:
				a.append(num[i][0])
		else:
			num[i],b=singleitem(num[i])
			#print 'num[i]= ',num[i]

	return num,a

def test(count,min,max):
	test=[]
	for i in range(count):
		test.append(random.randint(min,max))
	return test


while True:
	a=[]
	b=[]
	num=raw_input('\nnumbers list: ')
	print ''
	#num=num.split(' ')
	num=filter(lambda x:x!='',num.split(' '))
	if num[0]=='test':
		num=test(int(num[1]),int(num[2]),int(num[3]))
	else:
		for i in range(len(num)):
			num[i]=int(num[i])

	#print quicksort(num)
	time_1=time.time()
	num_delete,a=singleitem(num)
	time_2=time.time()
	print 'time:',time_2-time_1
    
	print num
	time_1=time.time()
	num.sort()
	time_2=time.time()
	print num
	print 'time:',time_2-time_1
	#print 'finalsort:',a




	print ''

    

