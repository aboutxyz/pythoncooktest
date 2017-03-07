#coding:utf-8

#解压可迭代对象
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

class Record:
    def __init__(self, name, email , *phone_no):
        self.name = name
        self.email = email
        self.phone_no = phone_no
        
d1 = Record(*record)
d1.name

#固定长度队列，保留历史纪录
from collections import deque
q = deque(maxlen = 3)
q.append(2)
q.appendleft(3)
q.pop()
q.popleft()

#查找最大或最小的N个元素
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
sorted(nums)[-3:] #返回最大的三个元素
sorted(nums)[::-1] #倒序

#简单优先级队列
import heapq
        
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
        
    def push(self, item , priority):
        heapq.heappush(self._queue, (-priority,self._index, item))
        
    def pop(self):
        return heapq.heappop(self._queue)[-1]

q = PriorityQueue()
q.push('a', 1) 
q.push('b',2)
q.pop()

#一个键映射多个值
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a']
s = {}
s['a'] = [1]
s['a'].append(2)
s['a']

#字典排序
from collections import OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
#A = 1 B = 2 C= 3 ~AA = 27
reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))    #s为字符 EXCEL数字

#字典的最大值
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
    'FBf': 10.75
    }
max(zip(prices.values(), prices.keys()))
sorted(prices)
sorted(prices.iteritems(), key = lambda x:x[1])

#字典的相同部分
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
a.viewitems() & b.viewitems()
a.viewitems() - b.viewitems(), 
a.viewitems() | b.viewitems()
a.viewitems() ^ b.viewitems()   #对称差集

c = {key:a[key] for key in a.viewkeys() - {'z', 'w'}}

#删除序列相同元素并保持顺序
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(dedupe(a, key=lambda d: (d['x'],d['y'])))
'''
with open('ff.txt','r') as f:   #删除重复行
    for line in dedupe(f):
        print line
'''

#命名切片
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2,6)
items[a]

#序列中出现次数最多的元素
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
word_counts.most_common(3)
max(zip(dict(word_counts).values(), dict(word_counts).keys()))

#通过某个关键字排序一个字典列表
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
sorted(rows, key = lambda x: (x['lname'], x['uid']))

#通过某个字段将记录分组
rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
'''
使用多值字典
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
for i in rows_by_date.iteritems():
    print i
'''
'''
使用groupby
from itertools import groupby
rows.sort(key = lambda x:x['date'])
for date, items in groupby(rows, key = lambda x:x['date']):
    print date
    for i in items:
        print i
'''

#从字典提取子集
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
p = {k:v for k,v in prices.iteritems() if v>200}
print p




