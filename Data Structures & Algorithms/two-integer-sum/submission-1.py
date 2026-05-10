class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valDict = {}

        for i in range(len(nums)):
            sub = target - nums[i]

            if sub in valDict:
                return [valDict[sub], i]
            
            valDict[nums[i]] = i