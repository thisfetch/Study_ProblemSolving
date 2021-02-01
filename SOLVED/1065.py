num = int(input())
num_li = []
if num < 100:
    print(num)
elif num < 111 and num > 100:
    print("99")
else:
    count = 99
    for i in range(111, num + 1):
        if (int(i / 100)) - (int(i / 10 % 10)) == (int(i / 10 % 10)) - (int(i % 10)):
            count = count + 1
        else:
            pass
    
    print(count)