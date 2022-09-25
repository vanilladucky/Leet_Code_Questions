class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.count = 0
        self.size = k
        self.headidx = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            idx = (self.headidx + self.count) % self.size
            self.queue[idx] = value
            self.count += 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.headidx = (self.headidx + 1) % self.size
            self.count -= 1
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1 
        else:
            return self.queue[self.headidx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1 
        else:
            return self.queue[(self.headidx+self.count-1)%self.size]

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.count == self.size:
            return True
        else:
            return False
