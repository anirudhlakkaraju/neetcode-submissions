class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []

    def push(self, val: int) -> None:
        if not self.st or val < self.minst[-1]:
            self.minst.append(val)
        else:
            self.minst.append(self.minst[-1])

        self.st.append(val)

    def pop(self) -> None:
        self.minst.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
