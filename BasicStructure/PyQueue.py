# 내장 함수 queue를 사용하여 구현
import queue

q = queue.Queue()

q.put('a')
q.put('b')
q.put('c')

q.qsize() # 3
q.get() # 'a'
q.qsize() # 2

# 내장 함수 queue를 사용하여
# Last in First Out Queue 구현하기
import queue
q = queue.LifoQueue()
q.put("a")
q.put("b")

q.qsize()
q.get()

# 우선순위가 높은 큐가 먼저 나온다.
import queue

q = queue.PriorityQueue()
q.put((10, "a"))
q.put((5, "b"))
q.put((15, "c"))
q.qsize()    # 3

# 내장함수 사용하지 않고 
# enqueue, dequeue 구현하기

q_list = list()

def enqueue(data):
    q_list.append(data)

def dequeue():
    data = q_list[0]
    del q_list[0]
    return data

for i in range(10):
    enqueue(i)

print(q_list)     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
dequeue()         # 0
print(q_list)     # [1, 2, 3, 4, 5, 6, 7, 8, 9]
enqueue(11)       # 11
print(q_list)     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]