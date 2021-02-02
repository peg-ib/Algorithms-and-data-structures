import fileinput
import re

result = 0
for line in fileinput.input():
    result += sum(map(int, re.findall(r'[+-]?\d+', line)))

print(result)
