import fileinput
import re


class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Heap:
    def __init__(self):
        self.data = list()

    def __len__(self):
        return len(self.data)

    def __sift_up(self, index):
        while index > 0 and self.data[index].key > self.data[(index - 1) // 2].key:
            self.data[index], self.data[(index - 1) // 2] = self.data[(index - 1) // 2], self.data[index]
            index = (index - 1) // 2

    def __sift_down(self, index):
        while True:
            buf_index = index
            if 2 * index + 1 < len(self.data) and self.data[2 * index + 1].key > self.data[buf_index].key:
                buf_index = 2 * index + 1
            if 2 * index + 2 < len(self.data) and self.data[2 * index + 2].key > self.data[buf_index].key:
                buf_index = 2 * index + 2
            if buf_index == index:
                break
            self.data[index], self.data[buf_index] = self.data[buf_index], self.data[index]
            index = buf_index

    def get_max_key(self):
        return self.data[0].key if len(self.data) > 0 else -1

    def insert(self, value, key=None):
        if key is None:
            key = self.get_max_key() + 1
        element = Element(key, value)
        self.data.append(element)
        self.__sift_up(len(self.data) - 1)

    def pop(self):
        if len(self.data) == 0:
            raise Exception('underflow')
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        answer = self.data.pop()
        self.__sift_down(0)
        return answer.value


class Stack:
    def __init__(self):
        self.data = Heap()
        self.size = 0
        self.max_size = None

    def is_init(self):
        return False if self.max_size is None else True

    def set_size(self, max_size):
        self.max_size = max_size

    def push(self, value):
        if self.size + 1 > self.max_size:
            raise Exception('overflow')
        self.size += 1
        self.data.insert(value)

    def pop(self):
        result = self.data.pop()
        self.size -= 1
        return result

    def all_stack(self):
        if self.size == 0:
            raise Exception('empty')
        result = list()
        while len(self.data):
            result.append(self.data.pop())
        result.reverse()
        for i in range(len(result)):
            self.data.insert(result[i])
        return result


if __name__ == '__main__':
    stack = Stack()
    for line in fileinput.input():
        line = line.strip('\n')
        if line == '':
            continue
        elif re.match(r'^set_size \d+$', line) and not stack.is_init():
            command, size = line.split()
            stack.set_size(int(size))
        elif re.match(r'^pop$', line) and stack.is_init():
            try:
                print(stack.pop())
            except Exception as msg:
                print(msg)
        elif re.match(r'^print$', line) and stack.is_init():
            try:
                res = stack.all_stack()
                print(*res)
            except Exception as msg:
                print(msg)
        elif re.match(r'^push \S+$', line) and stack.is_init():
            command, val = line.split()
            try:
                stack.push(val)
            except Exception as msg:
                print(msg)
        else:
            print('error')
