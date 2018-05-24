# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request,FormRequest

class youyuan(scrapy.Spider):
    name = 'youyuan'
    allowed_domains = ["http://n.youyuan.com/"]
    start_urls = [
        'http://n.youyuan.com',
    ]
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'}


    def start_requests(self):
        return  [Request('http://n.youyuan.com/v20/login.html?from=5599"',meta={'cookiejar':1},callback=self.login)]

    def login(self, response):
        #print("response")
        print(response.body)
        Cookie1 = response.headers.getlist('Set-Cookie')
        print("cookie")
        print(Cookie1)
        data = {
            'username':'18519199894',
            'password':'Zp123456789',
            'from':'5599',

        }
        print('login')

        return [FormRequest.from_response(response,
                                          url='http://n.youyuan.com/v20/user/login.html',
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          headers=self.header,
                                          formdata=data,
                                          callback=self.next,
                                          )]


    def next(self,response):
        print("login after")
        print(response.body)
        Cookie1 = response.headers.getlist('Set-Cookie')
        print(Cookie1)
        pass
