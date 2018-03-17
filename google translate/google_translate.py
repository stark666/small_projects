#coding=utf-8
#谷歌翻译，早期JS算出的tk，现在还能用
import requests    
import execjs
import win32clipboard as wc
import win32con  
  
class Py4Js():  
      
    def __init__(self):  
        self.ctx = execjs.compile(""" 
        function TL(a) { 
        var k = ""; 
        var b = 406644; 
        var b1 = 3293161072; 
         
        var jd = "."; 
        var $b = "+-a^+6"; 
        var Zb = "+-3^+b+-f"; 
     
        for (var e = [], f = 0, g = 0; g < a.length; g++) { 
            var m = a.charCodeAt(g); 
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
            e[f++] = m >> 18 | 240, 
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
            e[f++] = m >> 6 & 63 | 128), 
            e[f++] = m & 63 | 128) 
        } 
        a = b; 
        for (f = 0; f < e.length; f++) a += e[f], 
        a = RL(a, $b); 
        a = RL(a, Zb); 
        a ^= b1 || 0; 
        0 > a && (a = (a & 2147483647) + 2147483648); 
        a %= 1E6; 
        return a.toString() + jd + (a ^ b) 
    }; 
     
    function RL(a, b) { 
        var t = "a"; 
        var Yb = "+"; 
        for (var c = 0; c < b.length - 2; c += 3) { 
            var d = b.charAt(c + 2), 
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d; 
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
        } 
        return a 
    } 
    """)  
          
    def getTk(self,text):  
        return self.ctx.call("TL",text) 


      
def translate_en_to_cn(tk,content):     
    if len(content) > 4891:      
        print(u"too long")      
        return    
  
    param = {'tk': tk, 'q': content}  
  
    result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en 
        &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss 
        &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param)  
  
    #返回的结果为Json，解析为一个嵌套列表
    # print result.json() 
    return result.json()[0][0][0]
    # for text in result.json():
    #     print text
    #     print '*'*120  
        # print text[0]  
       
      
def main(content):      
    js = Py4Js()       
    tk = js.getTk(content)      
    print translate_en_to_cn(tk,content)   


def stripclipboard():
    wc.OpenClipboard()
    txt=wc.GetClipboardData(win32con.CF_TEXT)
    # print [txt]
    # print txt
    # print '*'*120
    txt=txt.strip().replace("\r\n"," ")
    # txt=txt.replace('\n',' ')
    # txt=txt.strip().replace("\r\n"," ").replace("\n"," ").replace("\r"," ")
    wc.EmptyClipboard()
    wc.SetClipboardData(win32con.CF_TEXT,txt)
    wc.CloseClipboard()
    # print '*'*120
    # print txt
    return txt

          
if __name__ == "__main__":
    txt=stripclipboard()
    print txt
    print '\n'+'*'*120+'\n'      
    # content=raw_input(txt)
    # content.replace('\n','')
    main(txt)