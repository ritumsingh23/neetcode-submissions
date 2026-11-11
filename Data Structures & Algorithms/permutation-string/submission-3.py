class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Counter = {chr(ord("a")+i):0 for i in range(26)}
        s2Counter = {chr(ord("a")+i):0 for i in range(26)}

        for i in range(len(s1)):
            s1Counter[s1[i]] += 1
            s2Counter[s2[i]] += 1
        
        matches = 0
        for key, val in s1Counter.items():
            if val == s2Counter[key]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            s2Counter[s2[r]] += 1
            if s2Counter[s2[r]] == s1Counter[s2[r]]:
                matches += 1
            elif s2Counter[s2[r]] == s1Counter[s2[r]] + 1:
                matches -= 1

            s2Counter[s2[l]] -= 1
            if s2Counter[s2[l]] == s1Counter[s2[l]]:
                matches += 1
            elif s2Counter[s2[l]] == s1Counter[s2[l]] - 1:
                matches -= 1
            l += 1
        print(matches)
        return matches == 26

