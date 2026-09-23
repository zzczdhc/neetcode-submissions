class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        def get_count(num):
            return counts[num]

        ordered = sorted(counts, key = get_count,reverse = True)
        return ordered[:k]
                
        