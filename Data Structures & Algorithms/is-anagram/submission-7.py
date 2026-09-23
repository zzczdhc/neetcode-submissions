class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = dict()
        counts_t = dict()

        for i in s:
            if i not in counts_s:
                counts_s[i] = 1
            else:
                counts_s[i] += 1

        for j in t:
            if j not in counts_t:
                counts_t[j] = 1
            else:
                counts_t[j] += 1

        return counts_s == counts_t
        