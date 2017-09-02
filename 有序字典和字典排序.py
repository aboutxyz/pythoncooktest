#coding:utf-8

#有序字典
from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d

#字典排序
d = {'a':1,'b':6,'c':3}
sorted(d.iteritems(),key = lambda x:x[0])   #按照键排序
sorted(d.iteritems(),key = lambda x:x[1])   sorted(zip(d.itervalues(),d.iterkeys()))    #按照值排序
#通过某个关键字排序一个字典列表
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
sorted(rows, key = lambda x: (x['lname'], x['uid']))

python 3把 itervalues和iterkeys换成 values和keys