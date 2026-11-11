class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxLength = 0, 0
        dups = set()

        for r in range(len(s)):
            while s[r] in dups:
                dups.remove(s[l])
                l += 1
            dups.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength