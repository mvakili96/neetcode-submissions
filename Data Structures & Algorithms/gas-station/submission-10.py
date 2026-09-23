class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1 
        summ_this = 0
        start = 0
        for i in range(len(gas)):
            res = gas[i] - cost[i]
            summ_this += res

            if summ_this < 0:
                summ_this = 0
                start = i + 1
        return start 
            
            



        