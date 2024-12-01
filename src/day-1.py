from util import get_input, submit
from heapq import heappush, heappop

def findDistance(input: str) -> int: 
    
    def buildQueuesFromInput(input: list[str]) -> tuple[list[int], list[int]]: 
        _listA: list[int] = []
        _listB: list[int] = []
        for line in input.splitlines(): 
            [lineA, lineB] = line.split('   ')
            heappush(_listA, lineA)
            heappush(_listB, lineB)
        return [_listA, _listB]
    
    def calculateDistance(listA: list[int], listB: list[int]) -> int: 
        distance = 0
        while len(listA) != 0 and len(listB) != 0: 
            distance += abs(int(heappop(listA)) - int(heappop(listB)))
        return distance
          
    
    [listA, listB] = buildQueuesFromInput(input)
    return calculateDistance(listA, listB)

input = get_input(1).strip()
res = findDistance(input)
print(res)

# submit(1, 1, res)