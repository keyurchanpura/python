def fact(n):
    if n>0:
        return n*fact(n-1)
    else:
        return 1
n=int(input('enter value of n::'))
f = fact(n)
print('factorial is::',f)
