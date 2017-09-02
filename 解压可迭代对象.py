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