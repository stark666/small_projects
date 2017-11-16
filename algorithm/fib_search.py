slist=[0,1,16,24,35,47,59,62,73,88,99]



def fib_search(slist,key):
	list_l=len(slist)
	# print list_l
	fib=[]
	fib.append(0)
	fib.append(1)
	k=2

	while True:
		fib.append(fib[k-1]+fib[k-2])
		if list_l<=fib[k]-1:
			break
		k+=1

	for i in range(list_l,fib[k]):
		slist.append(slist[list_l-1])

	# print slist
	# print k

	low=0
	high=list_l-1


	while low<=high:
		mid=low+fib[k-1]-1
		if key<slist[mid]:
			high=mid-1
			k=k-1
		elif key>slist[mid]:
			low=mid+1
			k=k-2
		else:
			if mid<=list_l:
				return mid
			else:
				return list_l

print fib_search(slist,99)