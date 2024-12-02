from util import get_input, submit
from enum import Enum

Mode = Enum('MODE', [('INCREASING', 1), ('DECREASING', 2)])

CountingRegime = Enum('COUNTING_REGIME', [('STRICT', 1), ('RELAXED', 2)])

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

def calculateSafeReports(input: str, regime: CountingRegime) -> int:   
    numOfSafeReports = 0
    grid = input.splitlines()

    for row in grid:
        rowMode: Mode
        cells = row.split(' ')
        canCheatABit: bool
        distanceToPrevCell = 1

        if regime == CountingRegime.STRICT:
            canCheatABit = False
        else:
            canCheatABit = True

        for y, cell in enumerate(cells):
            if y == 0:
                continue
            else:
                prevCell = cells[y - distanceToPrevCell]
                
                if distanceToPrevCell == 2:
                    distanceToPrevCell = 1

                diff = getDiff(int(cell), int(prevCell))
                mode = getDiffMode(diff)

                if isDiffSafe(diff):
                    if y == 1:
                        rowMode = getDiffMode(diff)
                    else: 
                        if mode != rowMode:
                            if canCheatABit:
                                canCheatABit = False
                                distanceToPrevCell = 2
                            else:
                                break
                else:
                    if canCheatABit:
                        canCheatABit = False
                        distanceToPrevCell = 2
                    else:
                        break

                if y == len(cells) - 1:
                    numOfSafeReports += 1
                                       
    return numOfSafeReports

input = get_input(2).strip()
numOfSafeReports = calculateSafeReports(input, CountingRegime.STRICT)
numberOfSafeReportsRelaxedRegime = calculateSafeReports(input, CountingRegime.RELAXED)
print(numberOfSafeReportsRelaxedRegime)
# submit(2, 2, numberOfSafeReportsRelaxedRegime)