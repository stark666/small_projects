#coding=gbk

import urllib,urllib2,re,thread,time


 
#用正则表达式爬取糗事百科的段子，并实现去除带有的图片段子，且没每按一次回车键实现显示下一条段子
#写这程序的原理是先把网页爬下来，再解析匹配源代码中的段子，并把所有的带图片和不带图片的段子都进行保存
#再在输出段子时实现控制输出就能实现只输出不带图片的段子，并实现每按一次快捷键就显示下一个段子的内容
#就是好像每一页都有二十个段子的。。。。只爬下来十九。。。。
 
 
class QSBK():
    def __init__(self):
        self.url='http://www.qiushibaike.com/hot/page/'                 #基础网址
        self.user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'   #要添加的headers
        self.headers={'User-Agent':self.user_agent}
        self.item_joke=[]                                               #用来保存段子的列表
 
    #请求函数
    def request(self,page):
        request=urllib2.Request(self.url+str(page),headers=self.headers)
        response=urllib2.urlopen(request)
        return response.read().decode('utf-8')                      #将源代码进行编码转换为HTML格式
 
    #将获取到的网页和正则表达式进行匹配并返回匹配到的每个段子的信息列表
    def get_joke(self,content):
        try:
            pattern = re.compile('<.*?class="author.*?>.*?<a.*?<h2>(.*?)</h2>.*?<div.*?class="content".*?<span>(.*?)</span>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
            self.item_joke.append(re.findall(pattern, content))     #将获取到的每一页的段子追加到存储列表中
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
 
    #逻辑函数
    def logic(self):
        page=input('输入你想要进行爬取的页数:')
        for i in range(int(page)):
            content=self.request(i+1)
            self.get_joke(content)
 
        print('输出段子:')
        i=0                                         #用来记录无图的段子
        print('每按一次快捷键读取一条段子,按Q退出！')
        for items in self.item_joke:                #由于爬取到的数据返回是以列表形式返回一整夜的段子的，所以要用for循环嵌套进行输出
            for item in items:
                input_=input()
                if input_=='Q':
                    return
                if not re.search('img',item[2]):    #筛选无图的段子输出
                    i+=1
                    print('\n作者:'+str(item[0]),'\n内容:'+str(item[1])+'\n点赞人数:'+str(item[3]))
        print('\n段子输出完毕！\n段子数量为:',i)
 
qiushibaike=QSBK()
qiushibaike.logic()
		