from bs4 import BeautifulSoup
import urllib
from tqdm import tqdm
from mylog import MyLog as mylog

class wbsItem(object):
    Commentator = None
    Comment = None

class wbsSpider(object):
    def __init__(self):
        self.wbsList = []
    def getUrl(self,url):
        urls = []
        while True:
            try:
                res = urllib.request.urlopen(url)
                soup = self.BeautifulSoup(res,'lxml')
                tag = soup.find('div',attrs={'class':'center'})
                urls.append(url)
                url = tag.find('a',attrs={'class':'next'}).get('href')
            except:
                break
        return urls
    def spider(self,urls):
        for url in urls:
            res = self.getRensponseContent(url)
            soup = BeautifulSoup(res,'lxml')
            tags = soup.find('div',attrs={'class':'comment'})
            item = wbsItem()
            item.Commentator = tag
            with open('wbs.txt','w') as fp:


    def getRensponseContent(self,url):
        try:
            response = urllib.request.urlopen(url)
        except:
            self.log.error('Python 返回URL:%s 数据失败'%url)
        else:
            self.log.info('Python 返回URL:%s 数据成功'%url)
            return response.read()