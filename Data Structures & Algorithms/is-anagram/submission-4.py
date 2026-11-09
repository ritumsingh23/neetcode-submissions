class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = collections.Counter(s)
        dictT = collections.Counter(t)

        return dictS == dictT