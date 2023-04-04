class Stack:
    def __init__(self):
        self.stack_ = []

    def is_empty(self):
        return self.stack_ == []

    def push(self, elem):
        self.stack_.append(elem)

    def pop(self):
        return self.stack_.pop()

    def peek(self):
        return self.stack_[-1]

    def size(self):
        return len(self.stack_)

    def balance_check(self, line: str, brackets_open="([{<", brackets_close=")]}>"):
        if line[0] in brackets_close:
            return "Несбалансированно"
        for elem in line:
            if elem in brackets_open:
                self.push(elem)
            elif elem in brackets_close and not self.is_empty():
                if brackets_open.index(self.peek()) == brackets_close.index(elem):
                    self.pop()
                else:
                    return "Несбалансированно"
        return "Сбалансированно" if self.size() == 0 else "Несбалансированно"


if __name__ == "__main__":
    stack = Stack()
    print(stack.balance_check("{{[()]}}"))
