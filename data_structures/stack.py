class Stack(object):
    def __init__(self):
        self._a = []

    def is_empty(self):
        return len(self._a) == 0

    def peek(self):
        return self._a[-1]

    def push(self, x):
        self._a.append(x)

    def pop(self):
        return self._a.pop()

    def size(self):
        return len(self._a)


if __name__ == "__main__":
    s = Stack()
    print(s._a)
    s.push(10)
    print(s._a)
    s.push(5)
    print(s._a)
    print(s.peek())
    x = s.pop()
    print(x)
    print(s.peek())
    print(s.is_empty())
    s.pop()
    print(s.is_empty())
