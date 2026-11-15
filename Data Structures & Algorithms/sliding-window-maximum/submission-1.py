class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        res = []

        for i, val in enumerate(nums):
            heapq.heappush(maxHeap, (-1*val, i))

            while maxHeap[0][1] < i-k+1:
                heapq.heappop(maxHeap)
            
            if len(maxHeap) < k:
                continue
            res.append(maxHeap[0][0]*-1)
        
        return res