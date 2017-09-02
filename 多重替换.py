#coding:utf-8

repls = ('hello', 'goodbye'), ('world', 'earth')
s = 'hello, world'
print reduce(lambda a, kv: a.replace(*kv), repls, s)
