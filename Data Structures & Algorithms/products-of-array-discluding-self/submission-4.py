class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [1,2,4,6]
        forward = [1, 1, 2, 8]
        backward = [1, 6, 24, 48]
        ans = [48, 24, 12, 8]
        """

        forward = [1]
        backward = [1]

        for i in range(1, len(nums)):
            forward.append(forward[-1]*nums[i-1])
        
        for i in range(len(nums)-2, -1, -1):
            backward.append(backward[-1]*nums[i+1])
        
        length = len(nums)
        return [forward[i] * backward[length-1-i] for i in range(length)]