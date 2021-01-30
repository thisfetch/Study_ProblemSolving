num = int(input())
mylist = list(map(int, input().split()))
li_count = 0
if num == len(mylist):
    for tmplist in mylist:
        count = 0
        for i in range(1, tmplist + 1):
            if tmplist % i == 0:
                count += 1
            if count == 2:
                li_count += 1


print(li_count)