class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for i in s:
            if self.alphaNum(i):
                newStr += i
        l,r = 0,len(newStr)-1
        while l < r:
            if newStr[l].lower() != newStr[r].lower():
                return False
            l += 1
            r -= 1

        return True    

     

        # equivalent to .isalnum()
    def alphaNum(self,s):
        return(ord("A")<= ord(s) <= ord("Z") or
            ord("a")<= ord(s) <= ord("z") or 
            ord('0')<= ord(s) <= ord('9'))
