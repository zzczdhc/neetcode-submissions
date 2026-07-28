class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = {}
        store_t= {}
        for char in s:
            if char in store:
                store[char] += 1
            else:
                store[char] = 1 

        for char in t:
            if char in store_t:
                store_t[char] += 1
            else:
                store_t[char] = 1 

        return store == store_t   