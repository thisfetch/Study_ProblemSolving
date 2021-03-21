import sys

num = int(input())
arr = list(map(int, sys.stdin.readline().split()))
sum = int(input())
arr.sort()

count = 0
s = 0
e = num - 1

while s != e:
    tmp = arr[s] + arr[e]
    if tmp == sum:
        count += 1
        s += 1
    elif tmp > sum:
        e -= 1
    else:
        s += 1

print(count)
