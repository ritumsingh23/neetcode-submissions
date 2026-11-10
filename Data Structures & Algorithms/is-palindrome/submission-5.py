class Solution:
    def isPalindrome(self, s: str) -> bool:
        considerStr = ""
        for c in s:
            print(c, ord(c), ord('A'), ord('Z'))
            if (ord(c) in range(ord("a"), ord('z')+1) or
                ord(c) in range(ord("A"), ord("Z")+1) or
                ord(c) in range(ord("0"), ord("9")+1)):
                considerStr += c.lower()
        
        l, r = 0, len(considerStr)-1
        while l < r:
            if considerStr[l] != considerStr[r]:
                return False
            l += 1
            r -= 1
        return True