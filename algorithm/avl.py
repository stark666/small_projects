#coding=utf-8
class avl_node(object):
	# ""tring for node"""
	def __init__(self,num,lchild=None,rchild=None):
		# super(node, self).__init__()
		self.num=num
		self.lchild=lchild
		self.rchild=rchild
		self.matrix=[]

	def clr_lrchild(self):
		self.lchild=None
		self.rchild=None
    
	def rl_to_rr(self):  #check
		# node,node_r,node_r_r=sorted([self,self.rchild,self.rchild.lchild],key=lambda x:x.num,reverse=False)
		# for i in [self,self.rchild,self.rchild.lchild]:
		# 	# print type(i)
		# 	i.clr_lrchild()
			# i=2
		node,node_r,node_r_r=self,self.rchild.lchild,self.rchild
		self.rchild.lchild=None
		self.rchild=node_r
		self.rchild.rchild=node_r_r
		# print node.num,node_r.num,node_r_r.num
		# self=node
		# self.rchild=node_r
		# self.rchild.rchild=node_r_r
		# print self.num,self.lchild.num
		return self

	def lr_to_ll(self):   #check
		
		node,node_l,node_l_l=self,self.rchild.lchild,self.lchild
		# print node_l_l.rchild.num
		# self.lchild=None
		self.lchild.rchild=None
		# print node.num,node_l.num,node_l_l.num
		# self=node
		self.lchild=node_l
		self.lchild.lchild=node_l_l
		# print self.num,self.lchild.num
		return self

	def l_rotate(self):  #check
		# node,node_r=self,self.rchild
		if self.rchild.balance()>0:
			self.rchild=self.rchild.r_rotate()
		node,node_r=self,self.rchild
		# print node.rchild.num 
		# self.rchild=None
		if  not node_r.lchild:
			node.rchild=None
			node_r.lchild=node
		else:
			if self.depth()==2:
				node=node.rl_to_rr()
				node=node.l_rotate()
				return node
			else:
				# if node.depth()==2:
				# 	node=node.rl_to_rr()
				# 	return node.l_rotate()

				# if node_r.lchild.num>node.num:
				node.rchild=None
				tmp=node_r.lchild
				node_r.lchild=node
				node.rchild=tmp
				# else:
				# 	node.rchild=None
				# 	node_r.lchild.rchild=node
				# 	node_r.lchild=node_r.lchild.rl_to_rr()
				# 	node_r.lchild=node_r.lchild.l_rotate()
		return node_r

	def r_rotate(self): #check
		# node,node_l=self,self.lchild
		if self.lchild.balance()<0:
			self.lchild=self.lchild.l_rotate()
		node,node_l=self,self.lchild
		# self.lchild=None
		if  not node_l.rchild:
			node.lchild=None
			node_l.rchild=node
		else:
			if node.depth()==2:
				node=node.lr_to_ll()
				return node.r_rotate()
			else:
				# if node_l.rchild.num<node.num:
				node.lchild=None
				tmp=node_l.rchild
				node_l.rchild=node
				node.lchild=tmp
				# else:
				# 	node.lchild=None
				# 	node_l.rchild.lchild=node
				# 	node_l.rchild=node_l.rchild.lr_to_ll()
				# 	node_l.rchild=node_l.rchild.r_rotate()
		return node_l

	def depth__(self,count=0):  #check
		if self.lchild and not self.rchild:
			count+=1
			count=self.lchild.depth(count)
		if self.rchild and not self.lchild:
			count+=1
			count=self.rchild.depth(count)
		if self.lchild and self.rchild:
			count+=1
			tmp_l=self.lchild.depth(count)
			tmp_r=self.rchild.depth(count)
			count=max(tmp_l,tmp_r)
		return count

	def depth(self):      #good method
		if self==Null:
			return -1
		else:
			return 1+max(self.lchild.depth(),self.rchild.depth())

	def balance(self):   #check
		if self.lchild and not self.rchild:
			return self.lchild.depth()+1
		if self.rchild and not self.lchild:
			return -(self.rchild.depth()+1)
		if self.lchild and self.rchild:
			tmp_l=self.lchild.depth()
			tmp_r=self.rchild.depth()
			return tmp_l-tmp_r
		if not self.lchild and not self.rchild:
			return 0

	def display(self):
		dep=self.depth()
		mat_length=2**(dep+1)
		# tmp_row=['' for i in range(mat_length)]
		# dis_mat=[tmp_row for i in range(dep)]
		dis_mat=[]
		# tmp_row[mat_length/2]=self.num
		tmp=[self]
		while filter(lambda x:x!=' ',tmp):
			tmp_row=[' ' for i in range(mat_length)]
			tmp_length=len(tmp)
			for index,item in enumerate(tmp):
				if type(item)==type(self):
					# print 2*index+1,(2**tmp_length),(float(2*index+1)/float(2**tmp_length))*mat_length,item.num
					tmp_row[int((float(2*index+1)/float(2**tmp_length))*mat_length)]=item.num
				else:
					tmp_row[int((float(2*index+1)/float(2**tmp_length))*mat_length)]=' '
			# print tmp_row
			dis_mat.append(tmp_row)

			tmp_2=[]
			for i in tmp:
				if type(i)==type(self) and i.lchild:
					tmp_2.append(i.lchild)
				else:
					tmp_2.append(' ')
				if type(i)==type(self) and i.rchild:
					tmp_2.append(i.rchild)
				else:
					tmp_2.append(' ')
			tmp=tmp_2

		for i in dis_mat:
			for j in i:
				print j,
			print ''

			# dis_mat[dep-self.depth()][mat_length/2]=self.num
			# if self.lchild:
			# 	dis_mat[1][mat_length/2**2]=self.lchild.num
			# 	# self=self.lchild
			# if self.rchild:
			# 	dis_mat[1][mat_length/2+mat_length/2**2]=self.rchild.num
		# print self.num
		# if self.lchild:
		# 	print self.num,'lc',self.lchild.num
		# 	self.lchild.display()
		# if self.rchild:
		# 	print self.num,'rc',self.rchild.num
		# 	self.rchild.display()
# lrc=avl_node(8)
# lc=avl_node(7,None,lrc)
# node=avl_node(9,lc,None)

# node=node.r_rotate()
# print node.num,node.lchild.num,node.rchild.num

# rlc=avl_node(9)
# rc=avl_node(10,rlc,None)
# node=avl_node(7,None,rc)
# node=node.rl_to_rr()
# print node.num,node.rchild.num,node.rchild.rchild.num

# rlc=avl_node(2)
# rc=avl_node(4,rlc,None)
# lc=avl_node(1)
# node=avl_node(3,lc,rc)
# node=node.l_rotate()
# print node.num,node.lchild.num,node.lchild.lchild.num,node.lchild.rchild.num

# llc=avl_node(5)
# lc=avl_node(6,llc,None)
# node=avl_node(7,lc,None)
# node=node.r_rotate()
# print node.num,node.lchild.num,node.rchild.num
# tmp=avl_node(5.5)
# node.lchild.rchild=tmp
# print node.depth()
# print node.balance()
# rrc=avl_node(9)
# rc=avl_node(8,None,rrc)
# node=avl_node(7,None,rc)

# node=node.l_rotate()
# print node.num,node.lchild.num,node.rchild.num



# test=[3,2,1,4,5,6,7,10,9,8]
# test=[4,3,2,1,2.75,5]
test=[1,2,3,4,5,6,7,8,9,10,11,12]
test=map(lambda x:avl_node(num=x),test)

leaf_node=[]
root_node=test.pop(0)
all_node=[root_node]
leaf_node=[root_node]
while test:
	new_node=test.pop(0)
	

	# print 'len',len(leaf_node)

	# min_dis=abs(new_node.num-leaf_node[0].num)
	root_node=max(all_node,key=lambda x:x.depth())
	
	while True:
		if new_node.num<root_node.num:
			if  not root_node.lchild:
				root_node.lchild=new_node
				break
			else:
				root_node=root_node.lchild
		if new_node.num>root_node.num:
			if  not root_node.rchild:
				root_node.rchild=new_node
				break
			else:
				root_node=root_node.rchild


	all_node.append(new_node)
	# for node in leaf_node:
	# 	# print node.num,
	# 	if abs(new_node.num-node.num)<=min_dis:
	# 		closest_node=node
	# 		min_dis=abs(new_node.num-node.num)
	# if new_node.num>closest_node.num:
	# 	closest_node.rchild=new_node
	# else:
	# 	closest_node.lchild=new_node
	# leaf_node.remove(closest_node)

	# print 'new node: ',new_node.num,'leaf: ',closest_node.num

	tmp_node=[]
	for node in all_node:
		if node.balance()>1:
			tmp_node.append(node)
	if tmp_node:
		node=sorted(tmp_node,key=lambda x:x.depth(),reverse=False)[0]
		# print node.depth,
		if node==max(all_node,key=lambda x:x.depth()):
			# print 'toppppppppppp'
			node=node.r_rotate()
		else:	
			for i in all_node:
				if i.lchild==node:
					# if node.lchild.balance()<0:
					# 	node.lchild=node.lchild.l_rotate()
						
					i.lchild=node.r_rotate()
					break

				if i.rchild==node:
					# if node.lchild.balance()<0:
					# 	node.lchild=node.lchild.l_rotate()
						
					i.rchild=node.r_rotate()
					break

	tmp_node=[]
	for node in all_node:
		# print node.num,
		if node.balance()<-1:
			# print node.num,
			tmp_node.append(node)

	if tmp_node:
		node=sorted(tmp_node,key=lambda x:x.depth(),reverse=False)[0]
		# print 'head: ',node.num
		if node==max(all_node,key=lambda x:x.depth()):
			# print 'head: ',node.num
			node=node.l_rotate()
		else:	
			for i in all_node:
				if i.rchild==node:
					# if node.rchild.balance()>0:
					# 	node.rchild=node.rchild.r_rotate()
						# print '-'*40
						# node.rchild.display()
						# print '-'*40
				
					i.rchild=node.l_rotate()
					break

				if i.lchild==node:
					# if node.rchild.balance()>0:
					# 	node.rchild=node.rchild.r_rotate()
						# print '-'*40
						# node.rchild.display()
						# print '-'*40
				
					i.lchild=node.l_rotate()
					break


	
	leaf_node=[]		
	for node in all_node:
		if node.depth()==0:
			leaf_node.append(node)


	node=max(all_node,key=lambda x:x.depth())
	# print node.num,node.depth()
	node.display()
	print 20*'*'

# for i in leaf_node:
# 	print i.num

for i in all_node:
	print 'num: ',i.num,'depth: ', i.depth(),i.balance()
	# if i.num==8:
	# 	i.display()
node=max(all_node,key=lambda x:x.depth())
# print node.num,node.depth()
# node.display()



