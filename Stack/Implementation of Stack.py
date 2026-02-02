## stack implementation using list
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Popped = " , stack.pop())
print("Popped = ", stack.pop())

## stack implementation using deque 
from collections import deque
stack = deque()
stack.append(10) ## [10]
stack.append(20)  ## [10,20]
stack.append(30)  ## [10,20,30]
print("Popped = ",stack.pop()) ## Popped = 30
print("TOS = ",stack[-1]) ## TOS = 20

## stack implementation using the deque is same as list
## but POP operation is faster , so efficiency is more.

## stack implementation using custom class
class Stack:
    def __init__(self):
        self.container = []
    ## push 
    def push(self,item):
        self.container.append(item)
    ## empty 
    def is_empty(self):
        return len(self.container) == 0
    ## pop
    def pop(self):
        return self.container.pop() if not self.is_empty() else None
    ## TOS
    def top_of_stack(self):
        return self.container[-1] if not self.is_empty() else None 
    ## size 
    def size(self):
        return len(self.container)
    ## print
    def print_stack(self):
        return self.container
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.print_stack())
print("Popped = ",stack.pop())
print("TOS = ",stack.top_of_stack())
print(stack.print_stack())

