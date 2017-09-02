#coding:utf-8
from random import choice
gamedict = {"scissors":1, "rock": 2, "paper":3,"s":1,"r":2,"p":3}
n = 0
while n< 3:
    a = raw_input("please input SRP : ")
    b = choice(gamedict.keys())
    print b
    if a not in gamedict.iterkeys():
        print "please input the correct SRP"
    else:
        if (gamedict[a]-gamedict[b]+2)%3 == 0:
            print "win"
        elif (gamedict[a]-gamedict[b]+2)%3 == 1:
            print "lose"
        else:
            print "tie"
        n+=1

