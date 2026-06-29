class MinStack:

    def __init__(self):
        self._min = int(math.pow(2, 31) - 1)
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self._min = min(self._min, val)
        self.min_stack.append(self._min)
        self.stack.append(val)
        
    def pop(self) -> None:
        self.min_stack.pop()
        pop = self.stack.pop()
        if len(self.min_stack) > 0:
            self._min = self.min_stack[-1]
        else:
            self._min = int(math.pow(2, 31) - 1)
        return pop

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
