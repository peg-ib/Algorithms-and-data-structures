import re
import fileinput


class BinarySearch:
    def __init__(self):
        self.array = None

    def set(self, array):
        self.array = array

    def binary_search(self, value, left=None, right=None, answer=None):
        if self.array is None:
            return
        if left is None:
            left = 0
        if right is None:
            right = len(self.array) - 1
        mid = (right + left) // 2
        if left > right:
            return answer
        elif self.array[mid] == value:
            answer = mid
        if self.array[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
        return self.binary_search(value, left, right, answer)


if __name__ == '__main__':
    b_s = BinarySearch()
    for line in fileinput.input():
        line = line.strip('\n')
        if line == '':
            continue
        elif re.search(r'^search [+-]?\d+$', line) is not None:
            command, val = line.split()
            index = b_s.binary_search(int(val))
            print(index if index is not None else -1)
        else:
            sequence = list(map(int, line.split()))
            b_s.set(sequence)
