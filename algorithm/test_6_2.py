#coding=gbk
#ϣ���㷨 ����
import time,random

def test(count,min,max):
	test=[]
	for i in range(count):
		test.append(random.randint(min,max))
	return test

def shell_sort(lists):
    # ϣ������
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
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
	lists=shell_sort(lists)
	time_2=time.time()
	print 'time:',time_2-time_1
				
	print lists
	#print '\nsort: ',num
	print ''