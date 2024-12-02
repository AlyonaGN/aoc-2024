from util import get_input, submit
from enum import Enum

def calculateSafeReports(input: str) -> int:
    Mode = Enum('MODE', [('INCREASING', 1), ('DECREASING', 2)])

    def getDiff(a: int, b: int) -> int:
        return a - b
    
    def isDiffSafe(diff: int) -> bool:
        absDiff = abs(diff)
        return absDiff >= 1 and absDiff <= 3
    
    def getDiffMode(diff: int) -> bool:
        if diff < 0:
            return Mode.DECREASING
        else:
            return Mode.INCREASING
        
    numOfSafeReports = 0
    grid = input.splitlines()

    for row in grid:
        rowMode: Mode
        cells = row.split(' ')

        for y, cell in enumerate(cells):
            if y == 0:
                continue
            else:
                prevCell = cells[y - 1]
                diff = getDiff(int(cell), int(prevCell))
                mode = getDiffMode(diff)

                if isDiffSafe(diff):
                    if y == 1:
                        rowMode = getDiffMode(diff)
                    else: 
                        if mode != rowMode:
                            break
                else:
                    break

                if y == len(cells) - 1:
                    numOfSafeReports += 1
                                       
    return numOfSafeReports

input = get_input(2).strip()
numOfSafeReports = calculateSafeReports(input)
print(numOfSafeReports)
# submit(2, 1, numOfSafeReports)