#coding=gbk
#堆排序

def max_heap(heap,heap_size,parent):
	left=2*parent+1
	right=2*parent+2
	max=parent
	if left<heap_size and heap[left]>heap[max]:
		max=left
	if right<heap_size and heap[right]>heap[max]:
		max=right
	if max!=parent:
		heap[max],heap[parent]=heap[parent],heap[max]
		max_heap(heap,heap_size,max)

	return heap
	

def build_max_heap(heap):
	heap_size=len(heap)
	#print heap_size
	for i in xrange((heap_size-2)/2,-1,-1):
		heap=max_heap(heap,heap_size,i)
		#print heap
	
	return heap

def heap_sort(heap):
	build_max_heap(heap)

	print '\nbuild max heap:',heap

	for i in range(len(heap)-1,-1,-1):
		print '\nbefore:',heap
		heap[0],heap[i]=heap[i],heap[0]
		print '\nbefore:',heap
		heap=max_heap(heap,i,0)
		print '\nafter max heap:',heap
		print '\n'
	return heap


if __name__=='__main__':
	heap=[30,50,57,77,62,78,94,80,84]
	print heap_sort(heap)
	#print max_heap(heap,len(heap),0)
	#print heap
	
