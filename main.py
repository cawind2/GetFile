#coding=utf-8
import os
import datetime

today = datetime.date.today()
print today
print('today is %s' % today.strftime("%Y%m%d"))
str_today = today.strftime("%Y%m%d")

filename = r'e:\log\192168115_DataEx\de_' + str_today + '.log'

try:
    file_object = open(filename)
    lastline = ''
    for line in file_object:
        if line:
            lastline = line
    print 'last line -> ' + lastline.decode('gbk')

    strs = ['2016-04-21',r'文件输出',r'停止',r'状态:完成']
    #print strs[1].decode('utf-8')

    if strs[0] in lastline.decode('gbk'):
        if strs[1].decode('utf-8') in lastline.decode('gbk'):
            if strs[2].decode('utf-8') in lastline.decode('gbk'):
                if strs[3].decode('utf-8') in lastline.decode('gbk'):
                    print r'2016-4-21 成功完成'
                else:
                    print '2016-4-21 出错'
            else:
                print '2016-4-21 出错'
        else:
            print '2016-4-21 出错'
    else:
        print '2016-4-21 出错'
    # file_object.seek(0)
    # alllines = file_object.read()
    # lastline = alllines[-2]
    # print lastline.decode('gbk')
    print '======='
except:
    print '文件没找到'
finally:
    file_object.close()