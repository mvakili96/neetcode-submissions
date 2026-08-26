class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stk = []
        for i,item in enumerate(temperatures):
            while stk and item > stk[-1][1]:
                out[stk[-1][0]] = i-stk[-1][0]
                stk.pop()
            stk.append([i,item])
        return out













        