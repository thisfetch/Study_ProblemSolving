num = int(input())
arr = []
arr_ = []
for i in range(num):
    arr.append(input().split())

for j in range(num):
    count = 0
    flag = 0
    arr_ = arr[j][1]
    for k in range(len(arr[j][1])):
        for l in range(int(arr[j][0])):
            print(arr_[k], end = "")
    print("")

# t = int(input())
# for i in range(t):
#     num, s = input().split() // 이렇게 따로 받을 수도 있다!
#     text = ''
#     for i in s:
#         text += int(num) * i
#     print(text)