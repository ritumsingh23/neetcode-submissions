class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        valAnagram = defaultdict(list)

        for i in range(len(strs)):
            alphabets = [0] * 26

            for c in strs[i]:
                alphabets[ord(c) - ord("a")] += 1
            
            valAnagram[tuple(alphabets)].append(strs[i])
        
        return list(valAnagram.values())

