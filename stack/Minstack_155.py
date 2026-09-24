class MinStack:

    def __init__(self):
        self.stack=[]
        self.Minstack=[]
        

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.Minstack:
            self.Minstack.append(value)
        elif value<self.Minstack[-1]:
            self.Minstack.append(value)
        else:    

            self.Minstack.append(self.Minstack[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.Minstack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.Minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()