#coding=gbk
#ѡ������

while True:
	num=raw_input('\nnumbers list: ')
	print ''
	num=num.split(' ')

	for i in range(len(num)):
		num[i]=int(num[i])

	for i in range(len(num)-1):
		num[i]=min(num[i+1:])
	
	print '\nsort: ',num
	print ''