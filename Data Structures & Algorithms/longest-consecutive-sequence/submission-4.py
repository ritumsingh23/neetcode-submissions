class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        numSet = set(nums)
        start = []

        for i in range(n):
            if nums[i] - 1 not in numSet:
                start.append(nums[i])

        for s in start:
            seqLength = 1
            while s + 1 in numSet:
                seqLength += 1
                s = s + 1
            ans = max(ans, seqLength)
        return ans
        
