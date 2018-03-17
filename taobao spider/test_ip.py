#coding=utf-8
#代理proxy

import urllib2,urllib,socket
from bs4 import BeautifulSoup

def check_ip_available(ip,soc):
	socket.setdefaulttimeout(3)
	url='http://ip.chinaz.com/getip.aspx'
	proxy_host='http://'+ip+':'+soc
	proxy_temp={'http':proxy_host}
	try:
		res=urllib.urlopen(url,proxies=proxy_temp).read()
		return res.decode('utf-8').encode('gbk')
		
	except Exception,e:
		pass
		#print e



def get_proxy(num=1):
	User_Agent='Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
	header={}
	header['User-Agent']=User_Agent

	url='http://www.xicidaili.com/nn/1'
	req=urllib2.Request(url,headers=header)
	res=urllib2.urlopen(req).read()

	soup=BeautifulSoup(res,'lxml')
	ips=soup.findAll('tr')

#	td=ips[num].findAll('td')
#	ip=td[1].contents[0]
#	soc=td[2].contents[0]
#	
#	ip_socket=check_ip_available(ip,soc)
#	if ip_socket and list(ip_socket)[0]=='{':
#		return ip_socket
#	else:
#		num+=1
#		print num
#		get_proxy(num)
		#return ip,soc,ip_socket


	#f=open('proxy','w')

	for i in range(1,len(ips)):
		td=ips[i].findAll('td')
		# print td
		ip=td[1].contents[0]
		soc=td[2].contents[0]
		ip_socket=check_ip_available(ip,soc)
	#	ip_socket=td[1].contents[0]+'\t'+td[2].contents[0]+'\n'
		if ip_socket:
			if list(ip_socket)[0]=='{':
				#print ip_socket
				return [ip,soc,ip_socket]
				#f.write(ip_socket+'\n')
	#f.close()

if __name__=='__main__':
	print get_proxy()

