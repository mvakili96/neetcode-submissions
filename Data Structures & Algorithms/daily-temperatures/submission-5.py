class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stk = [[0,temperatures[0]]]
        for i in range(1,len(temperatures)):
            if temperatures[i] > temperatures[i-1]:
                stk.pop()
                out[i-1] = 1
                while stk:
                    if temperatures[i] > stk[-1][1]:
                        out[stk[-1][0]] = i-stk[-1][0]
                        stk.pop()
                    else:
                        break

            stk.append([i,temperatures[i]])
        return out













        