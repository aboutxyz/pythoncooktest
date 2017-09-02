#coding:utf-8


#固定长度队列，保留历史纪录
from collections import deque
q = deque(maxlen = 3)
q.append(2)
q.appendleft(3)
q.pop()
q.popleft()