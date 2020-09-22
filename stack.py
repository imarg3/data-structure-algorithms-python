class Stack:
    def __init__(self, size):
        self.arr = [0] * size
        self.top = -1

    def push(self, value):
        self.top += 1
        self.arr[self.top] = value

    def pop(self):
        self.top = -1

    def peek(self):
        return self.arr[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.arr) - 1


def main():
    stack = Stack(6)
    stack.push(11)
    stack.push(22)
    stack.push(33)
    stack.push(44)

    value = stack.peek()
    print("Element on top = " + str(value) + "\n")

    while not stack.is_empty():
        value = stack.peek()
        stack.pop()
        print("Popped : " + str(value))


if __name__ == "__main__":
    main()
