#coding=gbk
#归并排序 快
import random,time

def test(count,min,max):
	test=[]
	for i in range(count):
		test.append(random.randint(min,max))
	return test

def merge(left,right):
	i,j=0,0
	result=[]
	while i<len(left) and j<len(right):
		if left[i]<right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	result+=left[i:]
	result+=right[j:]
	return result

def merge_sort(lists):
	if len(lists)<=1:
		return lists
	num=len(lists)/2
	left=merge_sort(lists[:num])
	right=merge_sort(lists[num:])
	return merge(left,right)

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
	lists=merge_sort(lists)
	time_2=time.time()
	print 'time:',time_2-time_1
				
	print lists
	#print '\nsort: ',num
	print ''
