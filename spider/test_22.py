#coding=gbk
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email import Encoders, Utils
import urllib2
import time
import re
import sys
import os

from bs4 import BeautifulSoup

from email.Header import Header

reload(sys)
sys.setdefaultencoding('utf-8')


class GetContent():
	def __init__(self, id):

		# �����ĵ�һ������ ������Ҫ���ص������id
		# ���� ��Ҫ���ص����������� https://www.zhihu.com/question/29372574
		# ��ô ������ python zhihu.py 29372574

		id_link = "/question/" + id
		self.getAnswer(id_link)

	def save2file(self, filename, content):
		# ����Ϊ�������ļ�
		filename = filename + ".txt"
		f = open(filename, 'a')
		f.write(content)
		f.close()

	def getAnswer(self, answerID):
		host = "http://www.zhihu.com"
		url = host + answerID
		print url
		user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0"
		# ����header αװһ��
		header = {"User-Agent": user_agent}
		req = urllib2.Request(url, headers=header)

		try:
			resp = urllib2.urlopen(req)
		except:
			print "Time out. Retry"
			time.sleep(30)
			# try to switch with proxy ip
			resp = urllib2.urlopen(req)
		# �����Ѿ���ȡ�� ��ҳ�Ĵ��룬������������ȡ����Ҫ�����ݡ� ʹ��beautifulSoup �������ܷ���
		try:
			bs = BeautifulSoup(resp,'lxml')

		except:
			print "Beautifulsoup error"
			return None
		
		#print bs.encode('gbk')
		title = bs.title
		print title
		# ��ȡ�ı���

		filename_old = title.string.strip()
		print filename_old
		filename = re.sub('[\/:*?"<>|]', '-', filename_old)
		# �����������ݵ��ļ�������Ϊ�ļ���������һЩ������ţ�����ʹ��������ʽ���˵�

		self.save2file(filename, title.string)


		detail = bs.find("div", class_="zm-editable-content")

		self.save2file(filename, "\n\n\n\n--------------------Detail----------------------\n\n")
		# ��ȡ����Ĳ�������

		if detail is not None:

			for i in detail.strings:
				self.save2file(filename, unicode(i))

		answer = bs.find_all("div", class_="zm-editable-content clearfix")
		k = 0
		index = 0
		for each_answer in answer:

			self.save2file(filename, "\n\n-------------------------answer %s via  -------------------------\n\n" % k)

			for a in each_answer.strings:
				# ѭ����ȡÿһ���𰸵����ݣ�Ȼ�󱣴浽�ļ���
				self.save2file(filename, unicode(a))
			k += 1
			index = index + 1

		smtp_server = 'smtp.126.com'
		from_mail = 'your@126.com'
		password = 'yourpassword'
		to_mail = 'yourname@kindle.cn'

		# send_kindle=MailAtt(smtp_server,from_mail,password,to_mail)
		# send_kindle.send_txt(filename)

		# ���÷����ʼ��������ѵ����鷢�͵����kindle�û��������˺ţ��������kindle�Ϳ����յ���������
		print filename


class MailAtt():
	def __init__(self, smtp_server, from_mail, password, to_mail):
		self.server = smtp_server
		self.username = from_mail.split("@")[0]
		self.from_mail = from_mail
		self.password = password
		self.to_mail = to_mail

		# ��ʼ����������

	def send_txt(self, filename):
		# ���﷢�͸�������Ҫע���ַ����룬��ʱ������ͦ�õģ���Ϊ�յ����ļ���������
		self.smtp = smtplib.SMTP()
		self.smtp.connect(self.server)
		self.smtp.login(self.username, self.password)
		self.msg = MIMEMultipart()
		self.msg['to'] = self.to_mail
		self.msg['from'] = self.from_mail
		self.msg['Subject'] = "Convert"
		self.filename = filename + ".txt"
		self.msg['Date'] = Utils.formatdate(localtime=1)
		content = open(self.filename.decode('utf-8'), 'rb').read()
		# print content
		self.att = MIMEText(content, 'base64', 'utf-8')
		self.att['Content-Type'] = 'application/octet-stream'
		# self.att["Content-Disposition"] = "attachment;filename=\"%s\"" %(self.filename.encode('gb2312'))
		self.att["Content-Disposition"] = "attachment;filename=\"%s\"" % Header(self.filename, 'gb2312')
		# print self.att["Content-Disposition"]
		self.msg.attach(self.att)

		self.smtp.sendmail(self.msg['from'], self.msg['to'], self.msg.as_string())
		self.smtp.quit()


if __name__ == "__main__":

	sub_folder = os.path.join(os.getcwd(), "content")
	# ר�����ڴ�����صĵ������Ŀ¼

	if not os.path.exists(sub_folder):
		os.mkdir(sub_folder)

	os.chdir(sub_folder)

	id = sys.argv[1]
	# �����ĵ�һ������ ������Ҫ���ص������id
	# ���� ��Ҫ���ص����������� https://www.zhihu.com/question/29372574
	# ��ô ������ python zhihu.py 29372574


	# id_link="/question/"+id
	obj = GetContent(id)
	# obj.getAnswer(id_link)

	# ���û�ȡ����

	print "Done"