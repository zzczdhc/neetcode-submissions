class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        seen2 = {}
        for c in s:
            seen1[c] = seen1.get(c,0)+1
        for c in t:
            seen2[c] = seen2.get(c,0) + 1

        if seen1 == seen2:
            return True

        else:
            return False


        