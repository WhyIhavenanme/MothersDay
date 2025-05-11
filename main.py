import math
import time
prout = ["2-","5O","2-","5O","2-","e","1-","9O","5O","1-","e","1-","9O","5O","1-","e","1-","9O","5O","1-","e","2-","9O","3O","2-","e","5-","6O","5-","e","7-","2o","7-"]
red = "\033[1;31m"
reset = "\033[0m"
for i in prout:
    cout=0
    if i=="e":
        print()
    else:
        while cout<int(i[0]):
            if i[1]=="O" or i[1]=="o":
                print(red,end='')
            print(i[1],end='')
            cout+=1
        print(reset,end='')
print()
print('\a',"母亲节快乐！")