import  scrapy
from scrapy import Selector

from scrapy_shares.items import DoubanItem


class douban(scrapy.Spider):
    name = "douban"
    allowed_domains = ["https://movie.douban.com"]
    start_urls = [
        'https://www.douban.com/doulist/2772079/?start=0&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=25&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=50&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=75&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=100&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=125&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=150&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=175&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=200&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=225&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=250&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=275&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=300&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=325&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=350&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=375&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=400&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=425&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=450&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=475&sort=seq&sub_type=',
        'https://www.douban.com/doulist/2772079/?start=500&sort=seq&sub_type='
    ]
    def parse(self, response):
        for movie in response.xpath('//*[@class="bd doulist-subject"]'):
            douban = DoubanItem()
            movieText = movie.extract()
            print(movieText)
            douban['title'] = Selector(text=movieText).xpath('//*[@class="title"]/a/text()').extract()[0]
            douban['time'] = Selector(text=movieText).xpath('//*[@class="abstract"]/text()[5]').extract()[0]
            douban['url'] = Selector(text=movieText).xpath('//*[@class="title"]/a/@href').extract()[0]
            douban['director'] = Selector(text=movieText).xpath('//*[@class="abstract"]/text()[1]').extract()[0]
            douban['score'] = Selector(text=movieText).xpath('//*[@class="rating_nums"]/text()[1]').extract()[0]
            yield douban
