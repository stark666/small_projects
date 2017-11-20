#coding=gbk

import  urllib2
from lxml import etree
from gooseeker import GsExtractor

class Spider: 
    def getContent(self, url): 
        conn = urllib2.request.urlopen(url) 
        output = etree.HTML(conn.read()) 
        return output 

    def saveContent(self, filepath, content): 
        file_obj = open(filepath, 'w', encoding='UTF-8') 
        file_obj.write(content) 
        file_obj.close()

bbsExtra = GsExtractor() 
# ����������gooseeker��api������xsltץȡ����
# ��һ��������app key���뵽GooSeeker��Ա��������
# �ڶ��������ǹ���������ͨ��GooSeeker��ͼ�λ�����: ı��̨MS �����ɵ�
bbsExtra.setXsltFromAPI("31d24931e043e2d5364d03b8ff9cc77e" , "���ӿͷ���������") 

url = "http://shenzhen.anjuke.com/tycoon/nanshan/p"
totalpages = 50
anjukeSpider = Spider()
print("��ȡ��ʼ")

for pagenumber in range(1 , totalpages): 
    currenturl = url + str(pagenumber) 
    print("������ȡ", currenturl) 
    content = anjukeSpider.getContent(currenturl) 
    outputxml = bbsExtra.extract(content) 
    outputfile = "result" + str(pagenumber) +".xml" 
    anjukeSpider.saveContent(outputfile , str(outputxml))

print("��ȡ����")