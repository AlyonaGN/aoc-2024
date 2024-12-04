

from util import get_input, submit
from functools import reduce


def countXmas(input: str) -> int:
    countDict = {
        'X': 0,
        'M': 0,
        'A': 0,
        'S': 0,         
    }

    for char in input:
        if char in countDict:
            countDict[char] += 1          
                
    return reduce(lambda a, b: a if a < b else b, countDict.values())


input = get_input(4).strip()
total = countXmas(input)
print(total)
submit(4, 1, total)