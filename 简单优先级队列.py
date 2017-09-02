#coding:utf-8


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