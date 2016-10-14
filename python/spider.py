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
reload(sys)
sys.setdefaultencoding( "utf-8" )
#定义数  
def chinese_patent(begin_page,end_page):   
    for i in range(begin_page, end_page):  
        print '正在下载第' + str(i) + '页'  
        f = open('专利公布重要数据','w+')  
        m = urllib2.urlopen(baseurl + str(i)).read()  
        f.write(m)  
        f.close()  
   
   
#-------- 在这里输入参数 ------------------  
#爬虫地址：http://epub.sipo.gov.cn/patentoutline.action?showType=0&strSources=pip&strWhere=浙江&numSortMethod=0&pageSize=10&pageNow=2  
baseurl = str('http://epub.sipo.gov.cn/patentoutline.action?showType=1&strSources=pip&strWhere=浙江&numSortMethod=0&pageSize=10&pageNow=')  
begin_page = int(raw_input(u'请输入开始的页数：\n'))  
end_page = int(raw_input(u'请输入终点的页数：\n'))  
#-------- 在这里输入参数 ------------------  
   
  
#调用  
chinese_patent(begin_page,end_page)  


