num = int(input())
for _ in range(num):
    stack = [] 
    paren = input()   
    for st in paren:
        if st == '(':
            stack.append(st)
        elif st == ')':
            if '(' not in stack:
                stack.append(st)
                break
            else:
                stack.pop()

    if '(' not in stack and len(stack) == 0:
        print("YES")
    else:
        print("NO")


