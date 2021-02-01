while 1:
    num = list(map(int, input()))
    if len(num) == 1 and num[0] == 0:
        break;
    flag = True
    for i in range(int(len(num) / 2)):
        if num[i] != num[len(num) - i - 1]:
            flag = False
    
    if flag == True:
        print("yes")
    else:
        print("no")
