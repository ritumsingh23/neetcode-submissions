class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxLength = 0, 0
        dups = {}

        for r in range(len(s)):
            dups[s[r]] = dups.get(s[r], 0) + 1
            if s[r] in dups:
                while dups[s[r]] > 1:
                    dups[s[l]] -= 1
                    l += 1
            maxLength = max(maxLength, r - l + 1)
        return maxLength