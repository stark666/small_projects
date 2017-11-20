from bs4 import BeautifulSoup
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup=BeautifulSoup(html,'html.parser')

#print 'title: ',soup.ttle,'\n'
#print 'head: ',soup.head,'\n'
#print 'a: ',soup.a,'\n'
#print 'p: ',soup.p,'\n'
#
#print soup.p.attrs
#print soup.p.name
#
#for i in soup.p.attrs:
#	print i,soup.p.attrs[i]

#for string in soup.strings:
#	print string

#print soup.head.title.string\

#print soup.find_all(id='link2')
#print soup.find_all(href=re.compile('elsie'))

print soup.find_all('a',class_='sister')
