#coding:utf-8

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

#排除键值
c = {key:a[key] for key in a.viewkeys() - {'z', 'w'}}

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