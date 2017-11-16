import random

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


head=random.randint(0,len(distance)-1)
print 'head:',head
print ''

con=[]

tmp_dis=[]
tmp_poi=[]
edge=[]
con.append(head)

while len(con)!=len(distance):
	tmp_dis=[]
	tmp_poi=[]
	for i in con:	
		for j in range(len(distance)):
			# print distance[0][8]
			if 0<distance[i][j]<INF and j not in con:
				tmp_dis.append(distance[i][j])
				tmp_poi.append([i,j])
	for k in tmp_poi:
		if distance[k[0]][k[1]]==min(tmp_dis):
			con.append(k[1])
			edge.append([k[0],k[1]])



print edge





