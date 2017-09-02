#coding:utf-8

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