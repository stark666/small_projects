#coding=utf-8

INF=65535

distance=[[0,1,5,INF,INF,INF,INF,INF,INF],
          [1,0,3,7,5,INF,INF,INF,INF],
          [5,3,0,INF,1,7,INF,INF,INF],
          [INF,7,INF,0,2,INF,3,INF,INF],
          [INF,5,1,2,0,3,6,9,INF],
          [INF,INF,7,INF,3,0,INF,5,INF],
          [INF,INF,INF,3,6,INF,0,2,7],
          [INF,INF,INF,INF,9,5,2,0,4],
          [INF,INF,INF,INF,INF,INF,7,4,0]]

p=range(len(distance))
proceed=[]
for i in range(len(p)):               #不可使用[p for i in range(len(p))]
	proceed.append([])                #会出现proceed[0][0]=4,使得proceed[1][0],proceed[2][0]...都等于4的情况
	for j in range(len(p)):     
		proceed[i].append(j)          #proceed存储从i到j的最短路径的第一步     
	
# print proceed

for k in range(len(distance)):
	for i in range(len(distance)):
		for j in range(len(distance)):
			if distance[i][j]>distance[i][k]+distance[k][j]:
				distance[i][j]=distance[i][k]+distance[k][j]
				proceed[i][j]=proceed[i][k]


for i in range(len(distance)):
	for j in range(len(distance)):
		print distance[i][j],
	print ''

for i in range(len(distance)):
	for j in range(len(distance)):
		print proceed[i][j],
	print ''