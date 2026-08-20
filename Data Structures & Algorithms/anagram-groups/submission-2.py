class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        for word in strs:
            wordCounter = [0 for _ in range(26)]
            for c in word:
                wordCounter[ord(c) - ord('a')] += 1
            if tuple(wordCounter) in wordDict:
                wordDict[tuple(wordCounter)].append(word)
            else:
                wordDict[tuple(wordCounter)] = [word]

        
        return list(wordDict.values())