class MinStack:

    def __init__(self):
        self.stack = []
        self.min = 2**31

    def push(self, val: int) -> None:
        if val < self.min:
            self.stack.append((val, val))
            self.min = val
        else:
            self.stack.append((val,self.min))

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min = self.stack[-1][1]
        else:
            self.min = 2**31

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
