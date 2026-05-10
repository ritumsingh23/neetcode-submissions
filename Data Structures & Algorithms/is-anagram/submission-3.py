class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tCounter = Counter(t)
        sCounter = Counter(s)

        return tCounter == sCounter