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
# 下面这句调用gooseeker的api来设置xslt抓取规则
# 第一个参数是app key，请到GooSeeker会员中心申请
# 第二个参数是规则名，是通过GooSeeker的图形化工具: 谋数台MS 来生成的
bbsExtra.setXsltFromAPI("31d24931e043e2d5364d03b8ff9cc77e" , "安居客房产经纪人") 

url = "http://shenzhen.anjuke.com/tycoon/nanshan/p"
totalpages = 50
anjukeSpider = Spider()
print("爬取开始")

for pagenumber in range(1 , totalpages): 
    currenturl = url + str(pagenumber) 
    print("正在爬取", currenturl) 
    content = anjukeSpider.getContent(currenturl) 
    outputxml = bbsExtra.extract(content) 
    outputfile = "result" + str(pagenumber) +".xml" 
    anjukeSpider.saveContent(outputfile , str(outputxml))

print("爬取结束")