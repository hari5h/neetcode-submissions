class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        minStackTopVal = self.minStack[-1] if len(self.minStack)  else float('inf')
        minVal = min(minStackTopVal, val)
        self.minStack.append(minVal)    
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]