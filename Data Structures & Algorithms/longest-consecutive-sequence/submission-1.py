class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        startPoints = []

        for i in range(len(nums)):
            if nums[i] - 1 not in numSet:
                startPoints.append(nums[i])
        
        res = 0
        for start in startPoints:
            longest_length = 1
            start_val = start
            while True:
                if start_val + 1 in numSet:
                    longest_length += 1
                    start_val += 1
                else:
                    break
            res = max(res, longest_length)
        
        return res
