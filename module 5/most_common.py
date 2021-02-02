def most_common(array):
    numbers = {}
    for element in array:
        if element in numbers.keys():
            numbers[element] += 1
        else:
            numbers[element] = 1
    max_number = None
    answer = []
    for key in numbers.keys():
        if max_number is None:
            max_number = numbers[key]
            answer.append(key)
            continue
        if numbers[key] is max_number:
            answer.append(key)
        elif numbers[key] > max_number:
            max_number = numbers[key]
            answer = [key]
    return min(answer)


if __name__ == '__main__':
    sequence = list(map(int, input().split()))
    print(most_common(sequence))
