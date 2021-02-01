from collections import deque

deq = deque()

num = int(input())

for i in range(num):
    deq.append(i + 1)

while len(deq) != 1:
    deq.popleft()
    n = deq.popleft()
    deq.append(n)

print(deq.pop())