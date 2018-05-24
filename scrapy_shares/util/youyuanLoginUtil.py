# -*- coding: utf-8 -*-
import  requests
from bs4 import BeautifulSoup


class youyuanLoginUtil:

    def __init__(self,username,password):
        self.headers = {
            'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            }
        self.session = requests.session()
        self.login_url = "http://n.youyuan.com/v20/user/login.html"
        self.start_url = "http://n.youyuan.com/v20/login.html?from=5599"
        self.index = "http://n.youyuan.com/v20/index.html"
        self.username = username
        self.password = password
        self.cookies = {}
        pass

    def getInfo(self):
        page = self.session.get(self.start_url, headers=self.headers)
        #soup = BeautifulSoup(page.text)
        response = self.session.post(self.login_url, data={'username': self.username,"password":self.password,"from":"5599"})
        self.cookies = response.cookies
        pass

    def login(self):
        print("login...")
        postdata = self.getInfo()
        print(postdata)
        pass


    def indexInfo(self):
        page = self.session.get(self.index, headers=self.headers,cookies=self.cookies)
        print(page.text)
        pass



if __name__ == '__main__':
    if __name__ == "__main__":
        username = '18519199894'
        password = '****'
        youyuan = youyuanLoginUtil(username, password)
        youyuan.login()
        youyuan.indexInfo()
