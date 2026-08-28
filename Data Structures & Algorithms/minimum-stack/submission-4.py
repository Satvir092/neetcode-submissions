class MinStack:

    def __init__(self):
        self.array = []
        self.length = 0

    def push(self, val: int) -> None:

        self.array.append(val)
        self.length += 1
        

    def pop(self) -> None:
        self.array.pop()
        self.length -= 1

    def top(self) -> int:
        return self.array[self.length - 1]

    def getMin(self) -> int:
        return min(self.array)
