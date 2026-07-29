class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            t = target - value
            if t in hashmap:
                return[hashmap[t],index]
            hashmap[value] = index
                


        