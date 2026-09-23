class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = dict()
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
            if counts[i] > 1:
                return True
        return False


        


        