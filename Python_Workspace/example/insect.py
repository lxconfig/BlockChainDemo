import urllib.request as ur
import urllib.parse as up
import re
import easygui as e
import socket  
from bs4 import BeautifulSoup

def find_download(h_soup,where,count):
      #下面的三条语句是为了分类，过滤取番号。没个网站的特点都不一样，要自己找规律。
      H = h_soup.find("h1",class_ = "article-title").a.get_text()
      if H[0] != "【" :
            try :#有些番号未知
                  str1 = h_soup.find("h2").span.span.get_text()
            except :
                  str1 = "404notfind%d"
      elif "【广告招租】" in H:
            return count
      else :
            str1 = ''
            for i in H:
                  str1 += i
                  if i == "】":
                        break
                  
      timeout = 10#设置下载被允许的最大时间
      for l in h_soup.find_all("img",class_ = re.compile("align.+"),src = re.compile(".[a-zA-Z]{3,4}$")):
            #下面的if是过滤四个垃圾图片 
            if l["src"] in ["http://ww1.sinaimg.cn/large/e75a115bgw1ezy20gtzgpj20m80b4gol.jpg","http://ww2.sinaimg.cn/mw690/e75a115bgw1f8ambv7odog20a00327h9.gif","http://ww3.sinaimg.cn/mw690/e75a115bgw1f76bno2v7kj20a0032wew.jpg","http://ww2.sinaimg.cn/mw690/e75a115bgw1ezm9k3vracj20by0by0tk.jpg"]:
                  continue
            url_fin = l["src"]
            for i in range(3):#网路或资源问题引发错误最多3次
                  try : 
                        request_fin = ur.Request(url_fin,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31'})#匿名
                        fin_img = ur.urlopen(request_fin,timeout = timeout).read()
                        break
                  except :
                        pass
            else :
                  continue
            file = open(where+"\"+"%s_%d.gif % (str1,count),'wb')
            file.write(fin_img)
            file.close()
            print("已下载:"+"\n"+"%s_%d.gif" % (str1,count))
            count += 1
      return count

            
def tryopen(req):#网路有错误最多5次
      errorTimes = 0 
      while errorTimes != 10:
            try: 
                  errorTimes += 1
                  return ur.urlopen(req,timeout = 10).read().decode("utf-8")
            except: 
                  pass
      return None
      

def main():
      if e.buttonbox("Are you ready?","黄虫",choices = ("of cause!","i'm Gay.")) == "of cause!":
            while 1:
                  have = e.multenterbox("输入你要的页数，如果只要一页就填一样的：","黄虫",fields = ("起始页","结束页"))
                  if have[0] != '' and have[1] != '':
                        nice = int(have[0])
                        day = int(have[1])
                        if nice > 1000 or day > 1000:
                              e.msgbox("绅士请注意身体！")
                              continue
                        break
                  e.msgbox("serious?")
            
            where = e.diropenbox("你要保存到哪？")
            i = nice
            while 1:#分三层 
                  url1 = "http://www.gifjia.com/neihan/page/%d/" % i
                  request1 = ur.Request(url1,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31'})#匿名
                  html1 = tryopen(request1)
                  h1_soup = BeautifulSoup(html1)#主页
                  text = '&&!@#$#@' #为了第一次能运行
                  word = 0#词条数
                  for j in h1_soup.find_all("a",href = re.compile("[0-9]+/$")):
                        if text in j["href"]: #为了防止重复爬，他网站有的url后面多点东西但是表示的和当前页面是同一个意思
                              continue
                        word += 1
                        if word > 11:#词条后面还有未知连接防止爬偏了。。11是因为前面还有一个废连接，一共10个词条。太不智能了。。。
                              break
                        url2 = j["href"]
                        text = url2
                        count = 0 #主页上每一个词条里的图片编号
                        request2 = ur.Request(url2,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31'})#匿名
                        html2 = tryopen(request2)
                        try :
                              h2_soup = BeautifulSoup(html2)#第一层连接副页
                              count = find_download(h2_soup,where,count)
                        except:
                              continue
                        for k in h2_soup.find_all("a",href = re.compile(j["href"]+"[0-9]+/")):
                              url3 = k["href"]
                              if j["href"]+"1/" == k["href"]:#防重复爬第一页
                                    continue
                              request3 = ur.Request(url3,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31'})#匿名
                              html3 = tryopen(request3)
                              try :                                    
                                    h3_soup = BeautifulSoup(html3)#副页还分好多页
                                    count = find_download(h3_soup,where,count)
                              except:
                                    pass
                  if i >= day:
                        break
                  i += 1                  
      else :
            e.msgbox("╭∩╮(︶︿︶)╭∩╮")
      

if __name__ == '__main__':
      main()
