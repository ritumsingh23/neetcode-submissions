class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [height[0]]
        rightMax = [0 for _ in range(len(height))]
        rightMax[-1] = height[-1]
        res = 0

        for i in range(len(height)):
            leftMax.append(max(leftMax[-1], height[i]))
        
        for i in range(len(height)-2, 0, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        
        for i, val in enumerate(zip(leftMax, rightMax)):
            waterStorage = min(val[0], val[1]) - height[i]
            res += waterStorage if waterStorage >= 0 else 0
        
        return res