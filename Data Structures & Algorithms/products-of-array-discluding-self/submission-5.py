class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwards = [1]
        backwards = [1]
        res = []

        for i in range(len(nums)-1):
            forwards.append(forwards[-1]*nums[i])
        
        for i in range(len(nums)-1, 0, -1):
            backwards.append(backwards[-1]*nums[i])

        for i in range(len(nums)):
            res.append(forwards[i]*backwards[len(nums)-1-i])
        
        return res