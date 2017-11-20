#coding=gbk

import urllib,urllib2,re,thread,time


 
#��������ʽ��ȡ���°ٿƵĶ��ӣ���ʵ��ȥ�����е�ͼƬ���ӣ���ûÿ��һ�λس���ʵ����ʾ��һ������
#д������ԭ�����Ȱ���ҳ���������ٽ���ƥ��Դ�����еĶ��ӣ��������еĴ�ͼƬ�Ͳ���ͼƬ�Ķ��Ӷ����б���
#�����������ʱʵ�ֿ����������ʵ��ֻ�������ͼƬ�Ķ��ӣ���ʵ��ÿ��һ�ο�ݼ�����ʾ��һ�����ӵ�����
#���Ǻ���ÿһҳ���ж�ʮ�����ӵġ�������ֻ������ʮ�š�������
 
 
class QSBK():
    def __init__(self):
        self.url='http://www.qiushibaike.com/hot/page/'                 #������ַ
        self.user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'   #Ҫ��ӵ�headers
        self.headers={'User-Agent':self.user_agent}
        self.item_joke=[]                                               #����������ӵ��б�
 
    #������
    def request(self,page):
        request=urllib2.Request(self.url+str(page),headers=self.headers)
        response=urllib2.urlopen(request)
        return response.read().decode('utf-8')                      #��Դ������б���ת��ΪHTML��ʽ
 
    #����ȡ������ҳ��������ʽ����ƥ�䲢����ƥ�䵽��ÿ�����ӵ���Ϣ�б�
    def get_joke(self,content):
        try:
            pattern = re.compile('<.*?class="author.*?>.*?<a.*?<h2>(.*?)</h2>.*?<div.*?class="content".*?<span>(.*?)</span>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
            self.item_joke.append(re.findall(pattern, content))     #����ȡ����ÿһҳ�Ķ���׷�ӵ��洢�б���
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
 
    #�߼�����
    def logic(self):
        page=input('��������Ҫ������ȡ��ҳ��:')
        for i in range(int(page)):
            content=self.request(i+1)
            self.get_joke(content)
 
        print('�������:')
        i=0                                         #������¼��ͼ�Ķ���
        print('ÿ��һ�ο�ݼ���ȡһ������,��Q�˳���')
        for items in self.item_joke:                #������ȡ�������ݷ��������б���ʽ����һ��ҹ�Ķ��ӵģ�����Ҫ��forѭ��Ƕ�׽������
            for item in items:
                input_=input()
                if input_=='Q':
                    return
                if not re.search('img',item[2]):    #ɸѡ��ͼ�Ķ������
                    i+=1
                    print('\n����:'+str(item[0]),'\n����:'+str(item[1])+'\n��������:'+str(item[3]))
        print('\n���������ϣ�\n��������Ϊ:',i)
 
qiushibaike=QSBK()
qiushibaike.logic()
		