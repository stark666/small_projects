import random
import numpy
import matplotlib.pyplot as plt

def get_pi(count):
	if float(count)/10000 in [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]:
		print 'count:',count
	#count=int(raw_input('count:'))
	#radius=int(raw_input('radius:'))
	num=0
	radius=2
	for i in xrange(count):
		x=random.uniform(0,radius)
		y=random.uniform(0,radius)
		if x**2+y**2<=radius**2:
			num+=1

	pi=4*float(num)/float(count)
	return pi
	#print 'pi:',pi,'\n'

if __name__=='__main__':
	t = range(5,100000,50)
	#print type(t)
	get_pi=[get_pi(i) for i in t]


	plt.figure()
	#plt.plot([1,2,3,4],[3,4,3,4],'g-')
	plt.plot(t,get_pi,"g-")
	#plt.plot(t,get_pi(t),"g-",label="$f(t)=e^{-t} \cdot \cos (2 \pi t)$")
	#plt.plot(t,f2(t),"r-.",label="$g(t)=\sin (2 \pi t) \cos (3 \pi t)$",linewidth=2)

	plt.axis([0,100000,3,3.5])
	plt.xlabel("count")
	plt.ylabel("pi")
	plt.title("a simple test")

	plt.grid(True)
	plt.legend()
	plt.show()