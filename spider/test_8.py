#coding=utf-8
#创建一个带有cookie的opener，在访问登录的URL时，
#将登录后的cookie保存下来，然后利用这个cookie来访问其他网址。

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
