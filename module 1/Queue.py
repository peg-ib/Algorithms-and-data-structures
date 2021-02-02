import sys


class Queue:
    def __init__(self, size):
        self._queue = [None for iteration in range(size)]
        self._size = size
        self._tail = 0
        self._head = 0

    def push(self, element_value):
        if self._tail == self._head and self._queue[self._head] is not None:
            raise Exception('overflow')
        else:
            self._queue[self._tail] = element_value
            self._tail += 1
            if self._tail == self._size:
                self._tail = 0

    def pop(self):
        if self._queue[self._head] is None:
            raise Exception('underflow')
        else:
            del_element = self._queue[self._head]
            self._queue[self._head] = None
            self._head += 1
            if self._head == self._size:
                self._head = 0
            return del_element

    def print(self):
        if self._queue[self._head] is None:
            return 'empty'
        if self._tail > self._head:
            return self._queue[self._head:self._tail]
        else:
            return self._queue[self._head:self._size] + self._queue[0:self._tail]


def parse_file(file_input, file_output):
    queue = None
    with open(file_input, 'r') as file_in:
        with open(file_output, 'w') as file_out:
            for line in file_in.readlines():
                line = line.strip('\n')
                if line == '':
                    continue
                elif line[:9] == 'set_size ' and line[9:].isdigit() and queue is None:
                    queue = Queue(int(line[9:]))
                elif line[:5] == 'push ' and line.count(' ') == 1 and queue is not None:
                    try:
                        queue.push(line[5:])
                    except Exception:
                        print('overflow', file=file_out)
                elif line == 'pop' and queue is not None:
                    try:
                        print(queue.pop(), file=file_out)
                    except Exception:
                        print('underflow', file=file_out)
                elif line == 'print' and queue is not None:
                    if type(queue.print()) == str:
                        print(queue.print(), file=file_out)
                    else:
                        print(*queue.print(), file=file_out)
                else:
                    print('error', file=file_out)


if __name__ == '__main__':
    input_file, output_file = sys.argv[1:]
    parse_file(input_file, output_file)

