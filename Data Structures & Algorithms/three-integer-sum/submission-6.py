class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # duplicate check for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                target = nums[i] + nums[j] + nums[k]
                # required used case when target == 0
                if target == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                # case where the target is greater than 0
                elif target > 0:
                    k -= 1
                # case where the target is less than 0
                else:
                    j += 1
                
        return res


                