class MyCircularDeque:

    def __init__(self, k: int):
        self.my_deque = list(-1 for _ in range(k))
        self.max_size = k
        self.first = k // 2 + 1
        self.last = k // 2
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.size >= self.max_size:
            return False
        self.my_deque[((self.first - 1) + self.max_size) % self.max_size] = value
        self.first = ((self.first - 1) + self.max_size) % self.max_size
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size >= self.max_size:
            return False
        self.my_deque[((self.last + 1) + self.max_size) % self.max_size] = value
        self.last = ((self.last + 1) + self.max_size) % self.max_size
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size <= 0:
            return False
        self.first = ((self.first + 1) + self.max_size) % self.max_size
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size <= 0:
            return False
        self.last = ((self.last - 1) + self.max_size) % self.max_size
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.size <= 0:
            return -1
        return self.my_deque[self.first]

    def getRear(self) -> int:
        if self.size <= 0:
            return -1
        return self.my_deque[self.last]

    def isEmpty(self) -> bool:
        return self.size <= 0

    def isFull(self) -> bool:
        return self.size >= self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
if __name__ == "__main__":
    pass
    # obj = MyCircularDeque(5)
    # param_1 = obj.insertFront(7)
    # param_2 = obj.insertLast(0)
    # param_3 = obj.getFront()
    # param_4 = obj.insertLast(3)
    # param_5 = obj.getFront()
    # param_6 = obj.insertFront(9)
    # param_7 = obj.insertFront()
    # param_8 = obj.getRear()
    # obj.getFront()
    # obj.getFront()
    # obj.deleteLast()
    # obj.getRear()

    # obj = MyCircularDeque(5)
    # param_1 = obj.insertFront(5)
    # param_2 = obj.insertFront(0)
    # param_3 = obj.insertLast(5)
    # param_4 = obj.deleteLast()
    # param_5 = obj.insertLast(7)
    # param_6 = obj.getFront()
    # param_7 = obj.deleteFront()
    # param_8 = obj.insertLast(6)
    # obj.insertLast(1)
