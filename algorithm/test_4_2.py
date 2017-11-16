#coding=gbk
import time,random

def test(count,min,max):
	test=[]
	for i in range(count):
		test.append(random.randint(min,max))
	return test

def quick_sort(lists, left, right):
    # 快速排序
    if right-left<=1:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


if __name__=='__main__':
	num=test(10000,1,100)
	time_1=time.time()
	num=quick_sort(num,0,len(num)-1)
	time_2=time.time()
	print num
	print 'time:',time_2-time_1


