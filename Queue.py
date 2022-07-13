
from collections import deque

class Queue:
    def __init__(self,initialList= []):
        self.container = deque(initialList)
    def enqueue(self,value):
        self.container.appendleft(value)
        return str(value)
    def dequeue(self):
        if self.isEmpty():
            return None
        return self.container.pop()
    def front(self):
        if self.isEmpty():
            print(self.container)
            return None
        return self.container[-1]
    def size(self):
        return len(self.container)
    def isEmpty(self):
        return self.size() <= 0




# myQueue=Queue([6,1,2])
# myQueue.enqueue(5)
# print(myQueue.container)


# Write a program to print binary numbers from 1 to 10 using Queue. 
# Use Queue class implemented in main tutorial. Binary sequence should look like
# 1
# #     10#     11#     100#     101#     110#     111#     1000#     1001#     1010
# # Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 
# and second number (i.e. 10) + 1.

# def binaryNumber():
#     binaryQueue = Queue()
#     binaryQueue.enqueue("1")
#     print(binaryQueue.container)
#     n=10
#     while(n > 0):
#         n -=1
#         s1 = binaryQueue.dequeue()
#         print (s1)
#         s2 = s1  
#         binaryQueue.enqueue(s1+"0")
#         binaryQueue.enqueue(s2+"1")

# print(binaryNumber())

