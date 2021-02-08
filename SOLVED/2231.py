num =int(input())
arr = []

for i in range(1,num):
    tmp= i
    ori = i
    
    while True:
        k = i % 10
        i = i // 10
        tmp = tmp + k

        if i / 10 == 0:
            if tmp == num:
                arr.append(ori)
            else: pass
            break
if not arr:
    print(0)
else:
    print(min(arr))

