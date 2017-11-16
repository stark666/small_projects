
class edge():
	def __init__(self,head,tail,weight): 
		self.head=head
		self.tail=tail
		self.weight=weight


INF=65535

distance=[[0,10,INF,INF,INF,11,INF,INF,INF],
          [10,0,18,INF,INF,INF,16,INF,12],
          [INF,INF,0,22,INF,INF,INF,INF,8],
          [INF,INF,22,0,20,INF,INF,16,21],
          [INF,INF,INF,20,0,26,INF,7,INF],
          [11,INF,INF,INF,26,0,17,INF,INF],
          [INF,16,INF,INF,INF,17,0,19,INF],
          [INF,INF,INF,16,7,INF,19,0,INF],
          [INF,12,8,21,INF,INF,INF,INF,0]]

edge_list=[]
road_list=[]
for i in range(len(distance)):
	for j in range(i,len(distance)):
		if 0<distance[i][j]<INF:
			p=edge(i,j,distance[i][j])
			edge_list.append(p)

edge_list.sort(key=lambda p:p.weight,reverse=True)
# for i in edge_list:
# 	print i.head,i.tail,i.weight


def no_loop(road_list):
	non_road=[]
	point={}

	for e in road_list:

		if e.head in point:
			point[e.head]+=1
		else:
			point[e.head]=1
		if e.tail in point:
			point[e.tail]+=1
		else:
			point[e.tail]=1

	print point
	print ''
	
	while len(filter(lambda x:point[x]==1,point)):
		for p in filter(lambda x:point[x]==1,point):
			for e in filter(lambda x:x not in non_road,road_list):


				if e.head==p or e.tail==p:
					point[e.head]-=1
					point[e.tail]-=1
					print point
					
					print ''
					non_road.append(e)
		count=0
		for i in point:
			if point[i]==0:
				count+=1
		if count==len(point):
			return True
	return False



def kruscal():

	p=edge_list.pop()
	# print p.head,p.tail,p.weight

	road_list.append(p)


	while edge_list:
		if no_loop(road_list):
			# print 'pass'
			p=edge_list.pop()
			road_list.append(p)
		else:
			# print 'lose'
			road_list.pop()

	if no_loop(road_list)==False:
		road_list.pop()


	for i in road_list:
		print i.head,i.tail
	print ''

kruscal()




	


