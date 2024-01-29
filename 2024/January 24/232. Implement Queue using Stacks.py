class MyQueue:

    def __init__(self):
        self.stack1 = []  
        self.stack2 = []  

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def transfer_elements(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

    def pop(self) -> int:
        self.transfer_elements()
        if self.stack2:
            return self.stack2.pop()
        else:
            raise Exception("Queue is empty")

    def peek(self) -> int:
        self.transfer_elements()
        if self.stack2:
            return self.stack2[-1]
        else:
            raise Exception("Queue is empty")

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
