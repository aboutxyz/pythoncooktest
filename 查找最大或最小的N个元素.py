#coding:utf-8

#查找最大或最小的N个元素
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
sorted(nums)[-3:] #返回最大的三个元素
sorted(nums)[::-1] #倒序

#查找最大或最小的N个元素
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heapq.heapify(nums)
nums[0]   #永远是最小的元素
heapq.nlargest(3,nums) #最大的三个元素
heapq.nsmallest(3,nums) #最小的三个元素
