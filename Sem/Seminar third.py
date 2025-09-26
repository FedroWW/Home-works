'''
from subprocess import check_output


def factorial(x):
    if x==1:
        return 1
    return x*factorial(x-1)
print(factorial(5))

def factorial_it(x):
    res=1
    for i in range(1,x+1):
        res*=i
    return res

print (factorial_it(5))

def fib(x):
 #f(0)=0 f(1)=1 f(n)=f(n-1)+f(n-2)
    if x==0:
     return 0
    if x==1:
        return 1
    return fib(x-1)+fib(x-2)

'''

'''
import time

t=time.time()
print (fib(100))
t=time.time()-t
print(t)
'''


'''
#с запоминанием
#cache(кэш)-список cache[n]=f(n)
#cache=[0*n]
def fib_memo(n,cache=[]):
    if n==0:
        return 0
    if n==1:
        return 1
    if cache[n]!=0:
        return cache[n]
    cache[n]=fib_memo(n-1,cache)+fib_memo(n-2,cache)
    return cache[n]

import time

t=time.time()
cache=[0]*51
print(fib_memo(50, cache))
t=time.time()-t
print(t)
'''

def func(x, symb):
    if x == 1:
        print(symb*((n-x)//2+1))
        return
    # то что до рекурсивного вызова
    # вызывается на прямом ходу рекурсии
    print(symb*((n-x)//2+1))
    func(x-2,symb)
    # то что после рекурсивного вызова
    # вызывается на обратном ходу рекурсии
    print(symb*((n-x)//2+1))

n = 7
s = '.'
func(n, s)