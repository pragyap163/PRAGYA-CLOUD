from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue:", queue)

queue.popleft()
print("Queue after dequeue:", queue)
