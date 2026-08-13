class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = []
        
    def push(self, val: int) -> None:
        if not self.min_:
            self.min_.append(val)
        else:
            self.min_.append(min(val,self.min_[-1]))

        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop(-1)
        self.min_.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_[-1]
        
