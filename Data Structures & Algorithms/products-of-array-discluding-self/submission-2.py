class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]

        for i in range(len(nums)-1):
            output.append(output[-1] * nums[i])
        
        mult = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * mult
            mult *= nums[i]
        
        return output
            