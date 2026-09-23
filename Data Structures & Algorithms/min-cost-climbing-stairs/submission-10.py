class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n =len(cost)
        cost[0] = cost[0]
        cost[1] = cost[1]
        for i in range(2,n):
            #到这里，付完钱，累计最低多少
            cost[i] = min(cost[i-1], cost[i-2])+cost[i]
        return min(cost[-1],cost[-2])
        