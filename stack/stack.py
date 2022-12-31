from collections import deque
stack = deque() #dequeu([])
stack.append(10) #deque([10])
stack.append(20) #deque([10,20])
stack.append(30) #deque([10,20,30])
print(stack.pop()) #deque([10,20])
top = stack[-1]
print(top)
size = len(stack)
print(size)