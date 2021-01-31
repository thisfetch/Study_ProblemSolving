import queue
cards = queue.Queue()
num = int(input())
for i in range(num):
    cards.put(i + 1)

print(cards)