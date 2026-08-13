class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost
        memo = set()
        def loss(i):
            if i >= len(cost)-2:
                return cost[i]
            
            if i not in memo:
                cost[i] += min(loss(i+1),loss(i+2))
                memo.add(i)
            
            return cost[i]

        return loss(0)


            
        



        