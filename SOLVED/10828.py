import sys 
num = int(sys.stdin.readline())
stack = []

for _ in range(num):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        stack.append(int(cmd[1]))

    elif cmd[0] == "pop":
        if not stack:
            print('-1')
        else:
            print(stack[-1])
            stack.pop()

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)

    elif cmd[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
