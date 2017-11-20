import urllib2
 
requset = urllib2.Request('http://www.2597919.com')
try:
	urllib2.urlopen(requset)
	print 'real website'
except urllib2.URLError as e:
	print e.reason