#coding=utf-8
#����һ������cookie��opener���ڷ��ʵ�¼��URLʱ��
#����¼���cookie����������Ȼ���������cookie������������ַ��

import urllib,urllib2,cookielib

filename='campus_net_cookie.txt'

cookie=cookielib.MozillaCookieJar(filename)
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata=urllib.urlencode({'stuid':'201200131012','pwd':'23342321'})

loginUrl='http://www.gg.com'
result=opener.open(loginUrl,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
gradeUrl='http://www.ggrade.com'
result=opener.open(gradeUrl)
print result.read()
