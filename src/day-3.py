from util import get_input, submit
import re

def multuply(input: str) -> int:
    muls = re.finditer(r"mul\(\d\d?\d?,\d\d?\d?\)", input, re.IGNORECASE)
    total = 0
    for mul in muls:
        total += int(re.search(r"\d\d?\d?", mul.group()).group())

    return total

input = get_input(3).strip()
res = multuply(input)
print(res)

submit(3, 1, res)