# -*- coding: utf-8 -*-  
#---------------------------------------  
#   程序：中国专利公布公告爬虫  
#   版本：0.1  
#   作者：why  
#   日期：2016-10-14  
#   语言：Python 2.7  
#   操作：根据分页操作,爬出重要的论文标题和内容,将其以文件的形式保存  
#---------------------------------------  
   
import string, urllib2  
import sys
import re
from HTMLParser import HTMLParser

reload(sys)
sys.setdefaultencoding( "utf-8" )

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_div = False

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            self.in_div = True
    
            
    def handle_data(self, data):
        if self.in_div == True and self.lasttag == 'li':
            if data.decode('utf-8') != '' and data.decode('utf-8').startswith("申请日") :
                print data.decode('utf-8')
            if data.decode('utf-8') != '' and data.decode('utf-8').startswith("申请人") :
                print data.decode('utf-8')
            if data.decode('utf-8') != '' and data.decode('utf-8').startswith("分类号") :
                print data.decode('utf-8')



#定义数  
def chinese_patent(begin_page,end_page):   
    for i in range(begin_page, end_page):  
        print 'spider is running  for page:' + str(i) 
        #f = open('patantContent','w+')
        m = str(urllib2.urlopen(baseurl + str(i)).read()).replace('&nbsp;','')
        parser = MyHTMLParser()
        parser.feed(m)
        #f.write(m)  
        #f.close()

def test_find():
    pattern = re.compile(r'^<div class="cp_linr"><h1>(.*?)</h1><ul>$')
    res = re.finditer(pattern, testStr)
    for match in res:
    	i = match.group().index('<h1>') + 4
    	j = match.group().index('</h1>')
        print match.group()[i:j].decode('utf-8')
   
def test_match():
    pattern = re.compile(r'^<div class="cp_linr"><h1>(.*?)</h1><ul>$')
    res = re.match(pattern, testStr) 
    print res.group(1).decode('utf-8')


#-------- 在这里输入参数 ------------------  
#爬虫地址：http://epub.sipo.gov.cn/patentoutline.action?showType=0&strSources=pip&strWhere=浙江&numSortMethod=0&pageSize=10&pageNow=2  
baseurl = str('http://epub.sipo.gov.cn/patentoutline.action?showType=1&strSources=pip&strWhere=AD%3dBETWEEN%5b%272001.01.01%27%2c%272010.12.31%27%5d+and+PA%3d%25%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6%25&numSortMethod=0&pageSize=10&pageNow=')  
begin_page = int(raw_input(u'Please input begin page:\n'))  
end_page = int(raw_input(u'Please input end page:\n'))  
#-------- 在这里输入参数 ------------------  

testStr  = str('<div class="cp_linr"><h1>[发明公布]一种浙江楠实生苗快速繁育方法</h1><ul>')
   
  
#调用  
#chinese_patent(begin_page,end_page)
if __name__ == "__main__":  
    chinese_patent(begin_page,end_page)

