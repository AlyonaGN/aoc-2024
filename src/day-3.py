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
    
    mulsDosDonts = re.finditer(r"(?:mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", input, re.IGNORECASE)
    total = 0
    canDo = True
    for m in mulsDosDonts:
        match = m.group()
        if (match.startswith("mul(")):
            if canDo:
                [intA, intB] = re.findall(r"\d{1,3}", match)
                total += int(intA) * int(intB)
        elif (match.startswith("do()")):
            canDo = True
        elif (match.startswith("don")):
            canDo = False

    return total

res2 = multiplyWithInstructions(input)
print(res2)
submit(3, 2, res2)