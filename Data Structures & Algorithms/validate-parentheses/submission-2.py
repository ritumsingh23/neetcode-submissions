class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"}":"{","]":"[",")":"("}

        stack = []

        for i in range(len(s)):
            if stack and s[i] in parentheses:
                if parentheses[s[i]] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        return True if stack == [] else False
                
            