from random import *
n=int(input('enter your password limit how you want print:'))
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit='0123456789'
for i in range(n):
    print(choice(alphabet+digit),choice(digit+alphabet),choice(alphabet+digit),choice(digit+alphabet),choice(alphabet+digit),choice(digit+alphabet),sep='')