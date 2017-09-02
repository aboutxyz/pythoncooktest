#coding:utf-8

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