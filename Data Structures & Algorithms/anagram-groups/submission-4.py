class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsDict = defaultdict(list)

        for s in strs:
            currAlpha = [0]*26
            for c in s:
                currAlpha[ord(c)-ord('a')] += 1
            anagramsDict[tuple(currAlpha)].append(s)
        return list(anagramsDict.values())