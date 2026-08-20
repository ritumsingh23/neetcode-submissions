class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {nums[0]: 0}

        for i in range(1, len(nums)):
            complement = target - nums[i]
            if complement in numDict:
                return [numDict[complement], i]
            numDict[nums[i]] = i