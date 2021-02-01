num = int(input())

su = 666
count = 0

while(True):
    if '666' in str(su):
        count += 1
        if count == num:
            print(su)
            break
    su += 1