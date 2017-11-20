#coding=gbk
#���棬ץȡ��������
import urllib,urllib2,re

class Tool:
	removeImg=re.compile('<img.*?>| {7}|')
	removeAddr=re.compile('<a.*?>|</a>')
	replaceLine=re.compile('<tr>|<div>|</div>|</p>')
	replaceTD=re.compile('<td>')
	replacePara=re.compile('<p.*?>')
	replaceBR=re.compile('<br><br>|<br>')
	removeExtraTag=re.compile('<.*?>')
	def replace(self,x):
		x=re.sub(self.removeImg,'',x)
		x=re.sub(self.removeAddr,'',x)
		x=re.sub(self.replaceLine,'\n',x)
		x=re.sub(self.replaceTD,'\t',x)
		x=re.sub(self.replacePara,'\n    ',x)
		x=re.sub(self.replaceBR,'\n',x)
		x=re.sub(self.removeExtraTag,'',x)
		return x.strip()

class BDTB:
	def __init__(self,baseUrl,seeLZ):
		self.baseURL=baseUrl
		self.seeLZ='?see_lz='+str(seeLZ)
		self.floorTag='1'
		self.floor=1

	def getPage(self,pageNum):    #��ø�ҳ�����
		try:
			url=self.baseURL+self.seeLZ+'&pn='+str(pageNum)
			request=urllib2.Request(url)
			response=urllib2.urlopen(request)
			#print response.read().decode('utf-8')
			return response.read()
		except urllib2.URLError,e:
			if hasattr(e,'reason'):
				print e.reason
				return

	def getTitle(self):           #��ñ���
		page=self.getPage(1)
		pattern=re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
		result=re.search(pattern,page)
		if result:
			#print result.group(1).decode('utf-8')
	
			return result.group(1).strip()
		else:
			return

	def getPageNum(self,page):
		pattern=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
		result=re.search(pattern,page)
		if result:
			return result.group(1).strip()
		else:
			return 
	
	def getContent(self,page):
		tool=Tool()
		#print page
		pattern=re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
		items=re.findall(pattern,page)
		print len(items)
		contents=[]
		for item in items:
			#print floor,'¥'+'='*110
			content='\n'+tool.replace(item.decode('utf-8'))+'\n'
			contents.append(content.encode('utf-8'))
		return contents

	def setFileTitle(self,title):
		if title:
			self.file=open(title+'.txt','a
			')
		else:
			self.file=open('NBA50.txt','w+')
	
	def writeData(self,contents):
		for item in contents:
			if self.floorTag=='1':
				floorLine='\n'+str(self.floor)+"-"*110
				self.file.write(floorLine)
			self.file.write(item)
			self.floor+=1

	def start(self):
		indexPage=self.getPage(1)
		pageNum=self.getPageNum(indexPage)
		title=self.getTitle()
		title=title.decode('utf-8')
		self.setFileTitle(title)
		if pageNum==None:
			print 'URL��ʧЧ��������'
			return
		try:
			print '�����ӹ���'+str(pageNum)+'ҳ'
			for i in range(1,int(pageNum)+1):
				print '����д���' + str(i)+'ҳ����'
				page=self.getPage(i)
				contents=self.getContent(page)
				self.writeData(contents)
		except IOError as e:
			print 'д���쳣��ԭ��'+e.message
		finally:
			print 'д���������'

baseURL='https://tieba.baidu.com/p/3138733512'
bdtb=BDTB(baseURL,1)
#bdtb.getContent(1)
#bdtb.getPage(1)
#print bdtb.getContent(1).decode('utf-8')
bdtb.start()

#<h3 class="core_title_txt pull-left text-overflow  " title="��ԭ�������е�NBA2014-2015��������50��" style="width: 396px">��ԭ�������е�NBA2014-2015��������50��</h3>