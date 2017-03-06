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
    'FB': 10.75
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
with open("C:\Users\user\Desktop\ff.txt",'r') as f:
    for line in dedupe(f):
        print line



