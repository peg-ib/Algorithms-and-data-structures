import re
import math


def search_max_index(sequence):
    for i in range(len(sequence) - 2, -1, -1):
        if sequence[i] < sequence[i + 1]:
            return i
    return


def search_index_bigger_element(sequence, element):
    for i in range(len(sequence) - 1, - 1, -1):
        if sequence[i] > element:
            return i
    return


def swap(sequence, i, j):
    sequence[i], sequence[j] = sequence[j], sequence[i]


def reverse_sequence(sequence, index):
    sequence = sequence[:index + 1:] + sequence[len(sequence) - 1:index:-1]
    return sequence


def permutation(sequence):
    result = []
    index = search_max_index(sequence)
    number_permutations = math.factorial(len(sequence))
    for count in range(number_permutations):
        result.append(str(sequence))
        element = sequence[index]
        swap_index = search_index_bigger_element(sequence, element)
        swap(sequence, index, swap_index)
        sequence = reverse_sequence(sequence, index)
        index = search_max_index(sequence)
        if index is None:
            result.append(str(sequence))
            sequence = sequence[::-1]
            index = search_max_index(sequence)
        if len(result) == number_permutations:
            break
    return result


def print_permutation(sequence):
    result_permutation = permutation(sequence)
    for numbers in result_permutation:
        numbers = numbers.strip('[]')
        print(re.sub(r'[,]', '', numbers))


if __name__ == '__main__':
    line = list(map(int, input().split()))
    print_permutation(line)
