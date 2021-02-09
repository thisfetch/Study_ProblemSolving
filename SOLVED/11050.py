from math import factorial
n , k = map(int,input().split())

if 0 <= k or k <= n:
    print(int(factorial(n)/ (factorial(k) * factorial(n-k))))
else:
    print(0)