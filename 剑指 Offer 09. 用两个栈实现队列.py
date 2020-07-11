class CQueue:
    def __init__(self):
        self.stack_in, self.stack_out = [], []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if len(self.stack_out):
            return self.stack_out.pop()
        else:
            if not len(self.stack_in):
                return -1
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

#用两个栈分别模拟尾进首出