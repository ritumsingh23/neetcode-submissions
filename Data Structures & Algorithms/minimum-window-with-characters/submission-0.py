class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        needs = collections.Counter(t)
        haves = {}
        matches = 0
        length, scope = float('inf'), [0, 0]

        l = 0
        for r in range(len(s)):
            haves[s[r]] = haves.get(s[r], 0) + 1

            if s[r] in needs and needs[s[r]] == haves[s[r]]:
                matches += 1
            
            while matches == len(needs):
                if r - l + 1 < length:
                    length = r - l + 1
                    scope = [l, r+1]

                haves[s[l]] -= 1
                if s[l] in needs and haves[s[l]] < needs[s[l]]:
                    matches -= 1

                if haves[s[l]] == 0:
                    haves.pop(s[l])
                
                l += 1
        
        return s[scope[0]:scope[1]] if length != float('inf') else ""
