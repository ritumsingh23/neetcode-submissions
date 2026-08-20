class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        numList = [[] for _ in range(len(nums))]
        ans = []
    
        for key, value in freq.items():
            numList[value-1].append(key)
        
        for i in range(len(numList)-1, -1, -1):
            if numList[i] != []:
                for n in numList[i]:
                    ans.append(n)
                    k -= 1
            
                    if k == 0:
                        return ans
        