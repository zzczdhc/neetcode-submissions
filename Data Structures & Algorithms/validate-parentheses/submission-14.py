class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(",
        ']':'[',
        '}':'{'}
        stack = []

        for char in s:
            if char not in pairs: # open parentheses
                stack.append(char)
            else: # close
                if not stack:
                    return False
                if pairs[char] != stack[-1]:
                    return False
                stack.pop()
        return len(stack)==0

        