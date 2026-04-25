class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        length = 0
        repDict = {}

        for r in range(len(s)):
            repDict[s[r]] = 1 + repDict.get(s[r], 0)
            while (r - l + 1) - max(repDict.values()) > k:
                repDict[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)

        return length