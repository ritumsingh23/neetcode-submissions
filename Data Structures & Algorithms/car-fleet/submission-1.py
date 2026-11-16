class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        prevTime = 0
        pairs = [(p,s) for p, s in zip(position, speed)]
        pairs.sort(reverse = True)
        fleets = 0

        for p,s in pairs:
            currTime = (target-p)/s
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        
        return fleets

