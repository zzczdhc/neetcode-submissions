class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char)-ord('a')] += 1
            result[tuple(counts)].append(word)

        return list(result.values())
        