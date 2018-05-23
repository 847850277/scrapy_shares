# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapySharesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()



#豆瓣实体类
class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    time = scrapy.Field()
    director = scrapy.Field()
    score = scrapy.Field()

    def __str__(self):
        return super(DoubanItem, self).__str__()




'''
if __name__ == '__main__':
    doubanItem = DoubanItem()
    doubanItem.director = 'aaa'
    print(doubanItem)
'''


