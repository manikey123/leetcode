from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        q = self.queue
        q.append(x)
        for _ in range(0,len(q) - 1):
            q.append(q.popleft())


    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue

# Test cases from LeetCode
myStack = MyStack()
myStack.push(1)
myStack.push(2)
# assert myStack.top() == 2  # return 2
# assert myStack.pop() == 2  # return 2
# assert not myStack.empty()  # return False

# Additional test cases
myStack.push(3)
assert myStack.top() == 3
assert myStack.pop() == 3
# assert myStack.empty()  == True # return True
