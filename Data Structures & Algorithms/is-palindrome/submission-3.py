class Solution:
    def isPalindrome(self, s: str) -> bool:
        validStr = ""
        value = list(range(65,91)) + list(range(48,58)) + list(range(97,123))
        valueSet = set(value)

        for c in s:
            if ord(c) in valueSet:
                validStr += c
        
        l, r = 0, len(validStr)-1

        while l < r:
            if validStr[l].lower() != validStr[r].lower():
                return False
            l += 1
            r -= 1
        
        return True