# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import MySQLdb
import datetime

DEBUG = True

if DEBUG:
    dbuser = 'root'
    dbpass = '2018P@ssword'
    dbname = 'crapy'
    dbhost = '59.110.158.56'
    dbport = '3306'
else:
    dbuser = 'root'
    dbpass = 'lihuipeng'
    dbname = 'game_main'
    dbhost = '127.0.0.1'
    dbport = '3306'


class ScrapySharesPipeline(object):
    def process_item(self, item, spider):
        return item



class DoubanPipline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()
        # 清空表：
        self.cursor.execute("truncate table douban;")
        self.conn.commit()
        print("bbbbbbbbb")



    def process_item(self,item,spider):
        print('begin insert data')
        try:
            self.cursor.execute("""INSERT INTO douban(title, score, time, director, url)  
                                       VALUES (%s, %s, %s, %s, %s)""",
                                (
                                    item['title'].encode('utf-8'),
                                    item['score'].encode('utf-8'),
                                    item['time'].encode('utf-8'),
                                    item['director'].encode('utf-8'),
                                    item['url'].encode('utf-8'),
                                )
                                )

            self.conn.commit()
            print('insert db success')

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        return item
