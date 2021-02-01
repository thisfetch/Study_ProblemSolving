# # LIFO
# class Stack(list):
#     def __init__(self):
#         self.stack = []

#     def push(self, data):
#         self.stack.append(data)
    
#     def pop(self):
#         if self.is_empty():
#             return -1
#         return self.stack.pop()
    
#     def peek(self):
#         return self.stack[-1]

#     def is_empty(self):
#         if len(self.stack) == 0:
#             return True
#         return False

# Singly linked list를 활용한 Stack 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return -1
        data = self.head.data
        self.head = self.head.next
        return data
    
    def is_empty(self):
        if self.head:
            return False
        return True
    
    def peek(self):
        if self.is_empty():
            return -1
        return self.head.data



if __name__=="__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())
    print(s.pop())
    print(s.pop())