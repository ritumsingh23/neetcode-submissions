class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = {}

        for i in range(len(numbers)):
            if numbers[i] in complement:
                return [complement[numbers[i]]+ 1, i+1]
            complement[target - numbers[i]] = i
        