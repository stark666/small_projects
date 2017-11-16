#coding=utf-8

INF=65535

distance_1=[[0,1,5,INF,INF,INF,INF,INF,INF],
          [1,0,3,7,5,INF,INF,INF,INF],
          [5,3,0,INF,1,7,INF,INF,INF],
          [INF,7,INF,0,2,INF,3,INF,INF],
          [INF,5,1,2,0,3,6,9,INF],
          [INF,INF,7,INF,3,0,INF,5,INF],
          [INF,INF,INF,3,6,INF,0,2,7],
          [INF,INF,INF,INF,9,5,2,0,4],
          [INF,INF,INF,INF,INF,INF,7,4,0]]


distance=[[0  ,2  ,5  ,INF,INF,INF,INF,INF,INF],
          [2  ,0  ,1  ,9  ,7  ,INF,INF,INF,INF],
          [5  ,1  ,0  ,INF,9  ,1  ,INF,INF,INF],
          [INF,9  ,INF,0  ,2  ,INF,9  ,INF,INF],
          [INF,7  ,9  ,2  ,0  ,5  ,2  ,7  ,INF],
          [INF,INF,1  ,INF,5  ,0  ,INF,6  ,INF],
          [INF,INF,INF,9  ,2  ,INF,0  ,9  ,8  ],
          [INF,INF,INF,INF,7  ,6  ,9  ,0  ,4  ],
          [INF,INF,INF,INF,INF,INF,8  ,4  ,0  ]]

dis=[0 for i in range(len(distance))]  #起点到各个结点的最短距离

s=[0]       #已取得最短距离的结点
tmp=[]      #存储尾结点有路径的附近节点
sw={}       #存储到每个节点的最短路径
#寻找离尾结点距离最近的结点
def find_shortest_point(point):
	# if 0<distance[point][final_point]<INF:
	# 	return final_point

	min=max(distance[point])
	for index,item in enumerate(distance[point]):
		if index not in s and item<min :
			min=item
			min_idx=index
			dis[index]=dis[point]+distance[point][index]
	return min_idx



#寻找s数组中是否有与next_point有连接
def find_shortest_dis(next_point,final_point):

	for index,item in enumerate(s):
		if 0<distance[item][next_point]<INF:
			tmp_dis=dis[item]+distance[item][next_point]
			if tmp_dis<=dis[next_point]:
				sw[next_point]=s[:index+1]+[next_point]
				dis[next_point]=tmp_dis

	s.append(next_point)


	print 's:',s
	print 'sw:',sw
	print 'dis:',dis
	print ''
	if s[-1]!=final_point:
		point=find_shortest_point(next_point)
		find_shortest_dis(point,final_point)
	left=set(range(len(distance)))-set(s)
	while len(left):
		left_point=left.pop()
		print 'left_point:',left_point
		for index,item in enumerate(s):
			if 0<distance[item][left_point]<INF:
				# print i,distance[i][left_point]
				tmp_dis=dis[item]+distance[item][left_point]
				# print tmp_dis,dis[left_point]
				if tmp_dis<=dis[left_point]:

					sw[left_point]=s[:index+1]+[left_point]
					dis[left_point]=tmp_dis
	print 'sw:',sw
	exit()
	




point=find_shortest_point(0)
print point
find_shortest_dis(point,8)




