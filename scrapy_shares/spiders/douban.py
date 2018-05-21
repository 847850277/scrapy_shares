import  scrapy


class douban(scrapy.Spider):
    name = "movie"
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
        movienames = response.xpath('//*[@class="doulist-item"]/div/div[2]/div[3]/a')
        for movie in movienames:
            print(movie.extract())
            #print(type(movie))
            #print(dir(movie))
