class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        matches = 0
        s1Dict = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
        s2Dict = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}

        for i in range(len(s1)):
            s1Dict[s1[i]] += 1
            s2Dict[s2[i]] += 1
        for i in range(ord('a'), ord('z')+1):
            if s1Dict[chr(i)] == s2Dict[chr(i)]:
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            s2Dict[s2[r]] += 1
            if s1Dict[s2[r]] == s2Dict[s2[r]]:
                matches += 1
            elif s1Dict[s2[r]] + 1 == s2Dict[s2[r]]:
                matches -= 1
            
            s2Dict[s2[l]] -= 1
            if s1Dict[s2[l]] == s2Dict[s2[l]]:
                matches += 1
            elif s1Dict[s2[l]] - 1 == s2Dict[s2[l]]:
                matches -= 1
            l += 1
        
        return True if matches == 26 else False