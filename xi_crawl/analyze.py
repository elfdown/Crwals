import pymysql
import time
import datetime
import jieba
import jieba.analyse
class sqlDocAnalyze:
    __doc_number__ = 0
    __data__ = []
    
    def __init__(self,tup):
        self.__data__ = list(tup)
        self.__doc_number__ = len(self.__data__)
    
    def __changeToDict__(self,tup):
        dic = {}
        dic['title'] = tup[3]
        dic['index'] = tup[0]
        dic['_index'] = tup[1]
        dic['type'] = tup[2]
        dic['time'] = tup[4]
        dic['length'] = tup[8]
        dic['source'] = tup[5]
        dic['editor'] = tup[6]
        dic['text'] = tup[7]
        return dic
        
    def __prettyPrint__(self,tup):
        dic = self.__changeToDict__(tup)
        print("---------------标题---------------\n{}".format(dic['title']))
        print("---------------序号---------------\n{}".format(dic['index']))
        print("---------------编号---------------\n{}".format(dic['_index']))
        print("---------------类型---------------\n{}".format(dic['type']))
        print("---------------发布时间:---------------\n{}".format(dic['time']))
        print("---------------文章长度---------------\n{}字".format(dic['length']))
        print("---------------来源---------------\n{}".format(dic['source']))
        print("---------------编辑---------------\n{}".format(dic['editor']))
        print("---------------内容---------------\n{}".format(dic['text']))
    
    def __jugdeDate__(self,date):
        date = str(date)
        date = date[:4]+'-'+date[4:6]+'-'+date[6:]
        try:
            time.strptime(date, "%Y-%m-%d")
            return True
        except:
            return False 
        
    def printDocNumber(self):
        print("这里总共拥有{}篇文章".format(self.__doc_number__))
        
    def printDoc(self,index=0):
        if index == 0:
            self.__prettyPrint__(self.__data__[0])
        elif index > self.__doc_number__ or index < 0:
            raise RuntimeError('index out of range')
        else:
            self.__prettyPrint__(self.__data__[index-1])

    def save(self,filepath,dic):
        with open (filepath,'w') as f:
            f.write("---------------\t  标题\t---------------\n{}\n".format(dic['title']))
            f.write("---------------\t  序号\t---------------\n{}\n".format(dic['index']))
            f.write("---------------\t  编号\t---------------\n{}\n".format(dic['_index']))
            f.write("---------------\t  类型\t---------------\n{}\n".format(dic['type']))
            f.write("---------------\t发布时间---------------\n{}\n".format(dic['time']))
            f.write("---------------\t文章长度---------------\n{}字\n".format(dic['length']))
            f.write("---------------\t  来源\t---------------\n{}\n".format(dic['source']))
            f.write("---------------\t  编辑\t---------------\n{}\n".format(dic['editor']))
            f.write("---------------\t  内容\t---------------\n{}\n".format(dic['text']))
            f.write("---------------文件保存时间---------------\n{}\n".format(time.strftime('%Y-%m-%d %H:%M',time.gmtime())))
        print('article is saved successfully at {}'.format(filepath))

    def saveByIndex(self,filepath,index):
        if index > self.__doc_number__ or index <= 0:
            raise RuntimeError('index out of range')
        else:
            tup = self.__data__[index-1]
            dic = self.__changeToDict__(tup)
            self.save(filepath,dic)
            print('No.{} article is saved successfully at {}'.format(index,filepath))

    def previewByDate(self,date1,date2):
        if date1 > date2:
            mid = date1
            date1 = date2
            date2 = mid
        if self.__jugdeDate__(date1) and self.__jugdeDate__(date2):
            flag = 0
            total = 0
            for info in self.__data__:
                dic = self.__changeToDict__(info)
                if eval(dic['time'].strftime('%Y%m%d')) >= date1 and eval(dic['time'].strftime('%Y%m%d')) <= date2:
                    flag = 1
                    total += 1
                    print("Index:{} time:{} title:{}".format(dic['index'],dic['time'],dic['title']))
            print('there are {} articles in total'.format(total))
            if not flag:
                print('no article is found')
        else:
            raise RuntimeError('illegal date')

    def startisticWordByDate(self,date1=10000101,date2=30000101,topK=10):
        if date1 > date2:
            mid = date1
            date1 = date2
            date2 = mid
        if self.__jugdeDate__(date1) and self.__jugdeDate__(date2):
            flag = 0
            word_str = ''
            total = 0
            for info in self.__data__:
                dic = self.__changeToDict__(info)
                if eval(dic['time'].strftime('%Y%m%d')) >= date1 and eval(dic['time'].strftime('%Y%m%d')) <= date2:
                    flag = 1
                    total += 1
                    word_str += dic['text']
            jieba.del_word("")
            word_list = jieba.lcut(word_str,cut_all=False)
            word_str = " ".join(word_list)
            word_tup = jieba.analyse.extract_tags(word_str, topK=topK, withWeight=True,allowPOS=['ns','n','vn','v'])
            return [word_tup,total]
            if not flag:
                print('no article is found')
        else:
            raise RuntimeError('illegal date')
        
    def startisticForDoc(self,dic,topK=10):
        word_str = dic['text']
        jieba.del_word("")
        word_list = jieba.lcut(word_str,cut_all=False)
        word_str = " ".join(word_list)
        word_tup = jieba.analyse.extract_tags(word_str, topK=topK, withWeight=True,allowPOS=['ns','n','vn','v'])

    def doc(self,index=0):
        if index == 0:
            dic = self.__changeToDict__(self.__data__[0])
            return dic
        elif index > self.__doc_number__ or index < 0:
            raise RuntimeError("index out of range")
        else:
            dic = self.__changeToDict__(self.__data__[index-1])
            return dic

if __name__ == "__main__":
    
    con = pymysql.connect(host='127.0.0.1',port=3306,user='root',db='xi',charset="utf8mb4")
    cursor = con.cursor()
    cursor.execute('SELECT * from `type7` where `type` = "原文"')
    result = cursor.fetchall()
    a = sqlDocAnalyze(result)
    a.saveByIndex('./test.txt',31580413)
    a.findByDate(20120101,20130101)