num = int(input())
arr = []
for i in range(num):
    arr.append(list(input().split()))
arr.sort(key = lambda x : int(x[0]))
for j, k in arr:
    print(j, k)