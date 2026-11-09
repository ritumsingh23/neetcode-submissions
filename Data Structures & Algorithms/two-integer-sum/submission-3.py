class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        used = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in used:
                return [used[complement], i]
            used[nums[i]] = i
        