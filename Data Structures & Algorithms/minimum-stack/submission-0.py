class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.appendleft(val)

    def pop(self) -> None:
        self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return min(self.stack)