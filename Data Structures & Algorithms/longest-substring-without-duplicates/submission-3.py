class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        dups = set()
        maxLen = 0

        for r in range(len(s)):
            while s[r] in dups:
                dups.remove(s[l])
                l += 1
            dups.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen