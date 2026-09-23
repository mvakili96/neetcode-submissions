class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        summ_whole = 0
        summ_this = 0
        start = 0
        for i in range(len(gas)):
            res = gas[i] - cost[i]
            summ_whole += res
            summ_this += res

            if summ_this < 0:
                summ_this = 0
                start = i + 1

        return start if summ_whole >= 0 else -1
            
            



        