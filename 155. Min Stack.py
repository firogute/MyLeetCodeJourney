class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("Stack is empty")


# Example usage
if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(3)
    min_stack.push(5)
    print(min_stack.getMin())  # Output: 3
    min_stack.push(2)
    min_stack.push(1)
    print(min_stack.getMin())  # Output: 1
    min_stack.pop()
    print(min_stack.getMin())  # Output: 2
    print(min_stack.top())      # Output: 2


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
