#coding=gbk
#ð�ݷ�

while True:
	num=raw_input('\nnumbers list: ')
	print ''
	num=num.split(' ')

	for i in range(len(num)):
		num[i]=int(num[i])
	#print num

	for i in range(len(num)):
		for j in range(len(num)-i-1):
			if num[j]>num[j+1]:
				temp=num[j]
				num[j]=num[j+1]
				num[j+1]=temp

	print '\nsort: ',num
	print ''