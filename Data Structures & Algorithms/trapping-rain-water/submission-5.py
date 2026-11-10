class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]
        suffix = [0]
        maxWater = 0
        n = len(height)

        for i in range(1,n):
            prefix.append(max(prefix[-1],height[i-1]))
        for i in range(n-2, -1, -1):
            suffix.append(max(suffix[-1],height[i+1]))
        
        for i in range(n):
            val = min(prefix[i],suffix[n-1-i])-height[i]
            maxWater += val if val > 0 else 0
        return maxWater
        
        