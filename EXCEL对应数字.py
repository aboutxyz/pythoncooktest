#coding:utf-8
#A = 1 B = 2 C= 3 ~AA = 27
str = "B"
print reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,str))


#coding:utf-8
@classmethod
class Solution(object):
    def convertToTitle(self, num):
        return "" if num == 0 else self.convertToTitle((num - 1) / 26) + chr((num - 1) % 26 + ord('A'))

convertToTitle(5)