class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(","]":"[","}":"{"}
        stack = []
        for i in s:
            if i in mapping: # if it is a close parenthese
                if stack and mapping[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(i)#open
        if stack:
            return False
        else:
            return True
        
                
