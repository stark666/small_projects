#coding=utf-8

import urllib,urllib2,re

page=1
url='http://www.qiushibaike.com/hot/page/'+str(page)
user_agent='Mozilla/4.0(compatible; MSIE 5.5;Windows NT)'
headers={'User-Agent':user_agent}
try:
	request=urllib2.Request(url,headers=headers)
	response=urllib2.urlopen(request)
	content=response.read().decode('utf-8').encode('GB18030')
	#print 'response done'
	pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+
                     '="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
	items = re.findall(pattern,content)
	for item in items:
			print item[0],item[1],item[2],item[3],item[4]
#		print '000000000000000',item[0]
#		print '111111111111111',item[1]
#		print '222222222222222',item[2]
#		print '333333333333333',item[3]
#		print '444444444444444',item[4]
except urllib2.URLError,e:
	if hasattr(e,'code'):
		print e.code
	if hasattr(e,'reason'):
		print e.reason