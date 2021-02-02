import fileinput


class Stack:

    def __init__(self, size):
        self.stack = [None for iteration in range(size)]
        self._size = size
        self.head = 0

    def push(self, element_value):
        if self.head is not self._size:
            self.stack[self.head] = element_value
            self.head += 1
        else:
            raise Exception('overflow')

    def pop(self):
        if self.head > 0:
            self.head -= 1
            print(self.stack[self.head])
        else:
            raise Exception('underflow')

    def print(self):
        if self.head > 0:
            print(*self.stack[:self.head])
        else:
            print('empty')


def parse_string(command_line):
    stack = None
    for line in command_line.input():
        line = line.strip('\n')
        if line == '':
            continue
        elif line[:9] == 'set_size ' and line[9:].isdigit() and stack is None:
            stack = Stack(int(line[9:]))
        elif line[:5] == 'push ' and line.count(' ') == 1 and stack is not None:
            try:
                stack.push(line[5:])
            except Exception:
                print('overflow')
        elif line == 'pop' and stack is not None:
            try:
                stack.pop()
            except Exception:
                print('underflow')
        elif line == 'print' and stack is not None:
            stack.print()
        else:
            print('error')


if __name__ == '__main__':
    parse_string(fileinput)
