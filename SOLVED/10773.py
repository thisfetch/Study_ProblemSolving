num = int(input())
stack = []
sum = 0
for _ in range(num):
    money = int(input())

    if money == 0:
        stack.pop()
    else:
        stack.append(money)

for st in stack:
    sum = sum + int(st)

print(sum)