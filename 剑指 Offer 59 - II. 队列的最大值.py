import collections

class MaxQueue:
    def __init__(self):
        self.queue = collections.deque()

    def max_value(self) -> int:
        if not self.queue:
            return -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)

    def pop_front(self) -> int:
        pop = self.queue.popleft()
        return pop