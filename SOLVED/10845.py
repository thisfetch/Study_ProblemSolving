import sys

num = sys.stdin.readline()
queue = []

for j in range(int(num)):
    comm = sys.stdin.readline().split() 
    if comm[0] == 'push':
        queue.append(comm[1])
    elif comm[0] == 'pop':
        if len(queue) !=0:
            print(queue.pop(0))
        else:
            print(-1)
    elif comm[0] == 'size':
        print(len(queue))
    elif comm[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif comm[0] == 'front':
        if len(queue) !=0:
            print(queue[0])
        else:
            print(-1)
    elif comm[0] == 'back':
        if len(queue) !=0:
            print(queue[-1])
        else:
            print(-1)
