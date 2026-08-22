class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsSorted = sorted(nums)
        ans = set()
        
        for i in range(len(numsSorted)):
            established = set()
            j = i + 1
            k = len(numsSorted)-1

            while j < k:
                if numsSorted[j] + numsSorted[k] + numsSorted[i] > 0:
                    k -= 1
                elif numsSorted[j] + numsSorted[k] + numsSorted[i] < 0:
                    j += 1
                else:
                    established.add((numsSorted[j], numsSorted[k]))
                    j += 1

            for items in established:
                ans.add((numsSorted[i], items[0], items[1]))
        
        res = []
        for val in ans:
            res.append([val[0], val[1], val[2]])

        return res

