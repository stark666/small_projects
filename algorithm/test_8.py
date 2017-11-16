#coding=gbk
#桶形算法 快速
import math
import random,time

def test(count,min,max):
	test=[]
	for i in range(count):
		test.append(random.randint(min,max))
	return test

def radix_sort(lists, radix=10):
	k = int(math.ceil(math.log(max(lists), radix)))
	bucket = [[] for i in range(radix)]
	for i in range(k+1):
		for j in lists:
			bucket[j/(radix**(i)) % radix].append(j)
			#print '\nbucket:',bucket
		del lists[:]
		for z in bucket:
			# print z
			lists += z
			# print z
			print ''
			#print '\nlists:',lists,'\n'
			del z[:]
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
	lists=radix_sort(lists)
	time_2=time.time()
	print 'time:',time_2-time_1
				
	print lists
	#print '\nsort: ',num
	print ''

