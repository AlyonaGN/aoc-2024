from util import get_input, submit
from queue import PriorityQueue

def findDistance(input: list[str]) -> int: 
    def buildQueuesFromInput(input: list[str]) -> tuple[PriorityQueue, PriorityQueue]: 
        _listA = PriorityQueue()
        _listB = PriorityQueue()
        for line in input.splitlines(): 
            [lineA, lineB] = line.split('   ')
            _listA.put(lineA)
            _listB.put(lineB)
        return [_listA, _listB]
    
    def calculateDistance(listA: PriorityQueue, listB: PriorityQueue) -> int: 
        distance = 0
        while not listA.empty() and not listB.empty(): 
            distance += abs(int(listA.get()) - int(listB.get()))
        return distance
          
    
    [listA, listB] = buildQueuesFromInput(input)
    return calculateDistance(listA, listB)

input = get_input(1).strip()
res = findDistance(input)
print(res)

submit(1, 1, res)