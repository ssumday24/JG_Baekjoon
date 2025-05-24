
def expt(b,n):
    if n==0: #b^0=1
        return 1
    else:
        return b * expt(b,n-1)

def square(n):
    return n*n

def fast_expt(b,n):
    if n==0:
        return 1
    
    else:
        if n%2 ==0:
            return square(expt(b,n/2)) 
        else : #홀수일때
            return b* expt(b,n-1)

def fib(n):
    if n==0:
        return 0
    if n==1: 
        return 1
    else:
        return fib(n-1)+fib(n-2)
    

##################################

max=0
idx=0

for i in range(9):
    n=int(input())
    if n>max:
        max=n
        idx=i
print(max)
print(idx+1)