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
distance = findDistance(input)

# submit(1, 1, distance)

def findSimilarity(input: str) -> int: 
    def parseInput(input: list[str]) -> tuple[list[int], dict[int, int]]: 
        _listA: list[int] = []
        _dictB: dict[int, int] = {}
        for line in input.splitlines(): 
            [lineA, lineB] = line.split('   ')
            _listA.append(lineA)
            if lineB not in _dictB: 
                _dictB[lineB] = 1
            else:
                _dictB[lineB] += 1
        return [_listA, _dictB]
    
    def calculateSimilarity(_listA, _dictB) -> int: 
        print(_listA, _dictB)
        similarity = 0
        for item in _listA: 
            if item in _dictB: 
                similarity += int(item) * _dictB[item]
                # prevent counting the same item multiple times
                del _dictB[item]
        return similarity
    
    [_listA, _dictB] = parseInput(input)
    return calculateSimilarity(_listA, _dictB)



input_2 = get_input(1).strip()
similarity = findSimilarity(input_2)

submit(1, 2, similarity)