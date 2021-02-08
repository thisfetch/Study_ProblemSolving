N, K = map(int, input().split())
arr = []
arr2= []
count = 0
idx = K - 1
for i in range(1, N+1):
    arr.append(i)

arr2.append(arr.pop(idx))
idx -=1 

while len(arr) != 0:
    count += 1
    idx += 1
    if idx > len(arr) - 1:
        idx = 0
    if count == K:
        arr2.append(arr.pop(idx))
        count = 0
        idx -= 1


print('<'+', '.join(map(str, arr2))+'>')