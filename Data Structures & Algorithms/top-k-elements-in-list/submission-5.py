class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = Counter(nums) # Counter({3: 3, 2: 2, 1: 1})
        bubble = [[] for _ in range(len(nums))]
        res = []

        for key,val in freqDict.items():
            bubble[val - 1].append(key)
        
        for i in range(len(bubble)-1, -1, -1):
            if bubble[i] != []:
                idx = 0
                while idx < len(bubble[i]) and k > 0:
                    res.append(bubble[i][idx])
                    idx += 1
                    k -= 1
        
        return res