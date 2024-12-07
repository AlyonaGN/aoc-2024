from util import get_input, submit
import re

def multiply(input: str) -> int:
    muls = re.finditer(r"mul\(\d\d?\d?,\d\d?\d?\)", input, re.IGNORECASE)
    total = 0
    for mul in muls:
        [intA, intB] = re.findall(r"\d\d?\d?", mul.group())
        total += int(intA) * int(intB)

    return total

input = get_input(3).strip()
res = multiply(input)

# submit(3, 1, res)

def multiplyWithInstructions(input: str) -> int:
    # try negative lookbehinds 
    # to-do: adjust for "do"
    muls = re.finditer(r"?<!\bdon't\b[a-z])mul\(\d\d?\d?,\d\d?\d?\)", input, re.IGNORECASE)
    total = 0
    for mul in muls:
        [intA, intB] = re.findall(r"\d\d?\d?", mul.group())
        total += int(intA) * int(intB)

    return total

res2 = multiplyWithInstructions(input)
print(res2)