'''
Created on 2022/10/14

@author: t20cs045
'''
import random

def hs(n):
    if n==0:
        print('グー',end='')
    elif n==1:
        print('チョキ',end='')
    elif n==2:
        print('パー',end='')

a=random.randrange(3)
b=random.randrange(3)

for x in range(2):
    if x==0:
        print('Aの手：', end='')
        hs(a)
    else:
        print(' v.s. Bの手：', end='')
        hs(b)
    
print(' ー＞ ',end='')

if a==b:
    print('引き分け')
elif (a==0 and b==1) or (a==1 and b==2) or (a==2 and b==0):
    print('Aの勝ち')
elif (a==0 and b==2) or (a==1 and b==0) or (a==2 and b==1):
    print('Bの勝ち')


    