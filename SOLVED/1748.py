import sys

num = int(sys.stdin.readline())
test = num
count = 1
sum = 0 

if num < 10:
    print(num)
else: 
    while test / 10 >= 10:
        test /= 10
        count += 1

    sum = ((int(num / 10 **count) -1) * (10 ** count) * (count + 1)) + ((num + 1) % (10 ** count) * (count + 1))

    for i in range(count):
        sum += 9 * (10 ** i) * (i + 1)

    print(sum)
