import xlrd

from datetime import date,datetime

class share_code(object):
    def __init__(self, code):
        self.code = code
        self.name = "name"

    def parseExcelAndGetAllCode(self):
        list = []
        excelFile = xlrd.open_workbook(r'/Users/zhengpeng/Downloads/a.xlsx')
        print excelFile.sheet_names()
        sheet = excelFile.sheet_by_name('a')
        rows = sheet.nrows
        for i in range(1,rows):
            rowvalue = sheet.row_values(i)
            map = {}
            for j in range(0,len(rowvalue)):
                if(j == 5):
                    print(rowvalue[j])
                    map['code'] = rowvalue[j]
                elif(j == 6):
                    print(rowvalue[j])
                    map['name'] = rowvalue[j]
            list.append(map)
        return list


    def buildAllFetchUrl(self):
        '''http: // disclosure.szse.cn / m / drgg_search.htm?secode ='''
        result = []
        list = self.parseExcelAndGetAllCode()
        for item in list:
            url = 'http://disclosure.szse.cn/m/drgg_search.htm?secode=' + item['code']
            result.append(url)
        return result


shareCode  = share_code(123)
print(shareCode.buildAllFetchUrl())


if __name__ == '__main__':
    pass
#codelist = shareCode.parseExcelAndGetAllCode()

#print(codelist)

#print(shareCode.name)
