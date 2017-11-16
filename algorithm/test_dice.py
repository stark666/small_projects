import random
import numpy
import matplotlib.pyplot as plt

def get_total(count,num):
	all_turn=[]
	for i in xrange(count):
		all_dice=0
		for j in xrange(num):
			all_dice+=random.randint(1,6)
		all_turn.append(all_dice)
			
	return all_turn

if __name__=='__main__':
	t=[]
	g=[]

	count=int(raw_input('how many times:'))
	num=int(raw_input('how many dices:'))

	get_total=get_total(count,num)
	get_total.sort()
	#print type(get_total)

	for i in get_total:
		if i not in t:
			t.append(i)
			g.append(1)
		else:
			g[-1]+=1

	
#	g=[0 for i in range(len(t))]
#
#	for i in get_total:
#		for j in range(len(t)):
#			if i==t[j]:
#				g[j]+=1


	plt.figure()
	#plt.plot([1,2,3,4],[3,4,3,4],'g-')
	plt.plot(t,g,"g-",label='%s %s'%(count,num))
	#plt.plot(t,get_pi(t),"g-",label="$f(t)=e^{-t} \cdot \cos (2 \pi t)$")
	#plt.plot(t,f2(t),"r-.",label="$g(t)=\sin (2 \pi t) \cos (3 \pi t)$",linewidth=2)

	plt.axis([min(t)*0.9,max(t)+min(t)*0.1,min(g)*0.9,max(g)+min(g)*0.1])
	plt.xlabel("count")
	plt.ylabel("pi")
	plt.title("a simple test")

	plt.grid(True)
	plt.legend()
	plt.show()