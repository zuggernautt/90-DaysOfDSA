# use two stacks to get minValue in O(1) else tc is O(n)

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            val = val
        else:
            val=min(val, self.minStack[-1])


        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
val= {2,3,4,5}
obj = MinStack()
obj.push(6)
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)