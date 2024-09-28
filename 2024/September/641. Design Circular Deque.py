class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head = None
        self.rear = None

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        newHead = Node(value, self.head)
        if self.head:
            self.head.prev = newHead
        else:
            self.rear = newHead  # First element case
        self.head = newHead
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        newRear = Node(value, None, self.rear)
        if self.rear:
            self.rear.next = newRear
        else:
            self.head = newRear  # First element case
        self.rear = newRear
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = self.rear = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.val

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.rear.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
