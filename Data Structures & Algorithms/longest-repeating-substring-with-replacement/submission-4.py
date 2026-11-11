class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        s = "AAABABB"
        freq = {A:1} | length = 1 | max = 1
        freq = {A:2} | length = 2 | max = 2
        freq = {A:3} | length = 3 | max = 3
        freq = {A:3,B:1} | length = 4 | max = 3
        freq = {A:4,B:1} | length = 5 | max = 4
        freq = {A:4,B:2} | length = 6 | max = 4
        """

        l = 0
        freq = {}
        maxFreq = 0
        ans = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])

            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1
                #maxFreq = max(maxFreq, freq[s[r]])
            ans = max(ans, r - l + 1)

        return ans