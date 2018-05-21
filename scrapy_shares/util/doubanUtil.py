from urlparse import urljoin

class doubanUtil(object):
    pass


    def buildUrl(self,url):
        print("this method is build url")
        list = []
        length = self.buildSize(25,525)
        for i in range(0,length):
            pageno = i*25
            newurl = (url.replace("{page}", str(pageno)))
            list.append(newurl)

        return list


    def buildSize(self,perSize,countSize):
        if(countSize % perSize == 0):
            return countSize/perSize
        else:
            return  (countSize/perSize + 1)


if __name__ == '__main__':
    doubanUtil = doubanUtil()
    url = "https://www.douban.com/doulist/2772079/?start={page}&sort=seq&sub_type="
    size = doubanUtil.buildSize(25,325)
    print(size)
    list = doubanUtil.buildUrl(url)
    print(list)

