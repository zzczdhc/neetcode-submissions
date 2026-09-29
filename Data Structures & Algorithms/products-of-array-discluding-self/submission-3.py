class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)

        prefix = [0]*len(nums)
        prefix[0] = nums[0]

        postfix = [0]*len(nums)
        postfix[-1] = nums[-1]

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i]
        for i in range(len(nums)-2,0,-1):
            postfix[i] = postfix[i+1]*nums[i]
        
        result[0] = postfix[2]
        result[-1] = prefix[-2]
        for i in range(1,len(nums)-1):
            result[i] = prefix[i-1]*postfix[i+1]

        return result




        