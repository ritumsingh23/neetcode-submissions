class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                temp, idx = stack.pop()
                res[idx] = i - idx
            
            stack.append((val, i))
        return res