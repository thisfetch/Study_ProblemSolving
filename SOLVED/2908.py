num1, num2 = map(str, input().split())
rnum1 = "".join(reversed(num1))
rnum2 = "".join(reversed(num2))
print(max(int(rnum1), int(rnum2)))
